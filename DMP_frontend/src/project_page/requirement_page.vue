<script>
import RequirementAdd from "../components/dialog/RequirementAdd.vue";
import ShowLinkData from "../components/dialog/ShowLinkData.vue";

export default {
  components: {ShowLinkData, RequirementAdd},
  data(){
    return{
      tableData:[],
      dialogVisible:false,
      showLinkVisible:false,
      pid:'',
      searchId:'',
      editOrAdd:'',
      editForm:[],
      stateSelectValue:'',
      stateOption:[{
        value: '未开始',
        label: '未开始'
      }, {
        value: '进行中',
        label: '进行中'
      }, {
        value: '已完成',
        label: '已完成'
      }, {
        value: '已延期',
        label: '已延期'
      }]
    }
  },
  created() {
    this.pid = sessionStorage.getItem('pid')
    this.getRequirementInfo(this.pid)
  },
  methods:{
    // 父组件接收到子组件val时，关闭dialog
    getVs(val) {
      this.dialogVisible=val
    },
    getShowLinkVs(val) {
      this.showLinkVisible=val
    },
    // 父组件接收到子组件传递的val时，触发搜索页面数据操作
    fresh(val){
      if (val) {
        this.getRequirementInfo(this.pid)
      }
    },
    // 通过session内存储的项目ID获取需求列表
    getRequirementInfo(pid) {
      this.$axios.get('api/project/requirement/info/',{
        params:{pid:pid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000'){
          this.tableData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 点击详情查询目标需求内容
    getEditRequirementForm(rid) {
      this.$axios.get('api/project/requirement/info/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000'){
          this.editForm = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 需求删除按钮
    delRequirement(rid) {
      this.$axios.get('api/project/requirement/del/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('删除成功')
          this.getRequirementInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 更新需求状态
    stateChange(rid,newState) {
      this.$axios.post('api/project/requirement/updateState/',{
        rid:rid,newState:newState
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.getRequirementInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
  },
}
</script>

<template>
<div>
  <div style="margin-bottom: 10px">
    <el-button
      type="primary"
      size="small"
      icon="el-icon-circle-plus-outline"
      @click="dialogVisible=true;editOrAdd='add'"
      >
      创建需求
    </el-button>
    <el-dropdown>
      <el-button type="primary" plain size="small">更多操作<i class="el-icon-arrow-down el-icon--right"></i></el-button>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-upload2">导入需求</el-dropdown-item>
        <el-dropdown-item icon="el-icon-download">导出需求</el-dropdown-item>
        <el-dropdown-item icon="el-icon-link">关联用例</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
  <div>
    <el-card>
      <el-table :data="tableData" max-height="70vh" style="width: 100%;min-height: 65vh">
        <el-table-column
          label="#"
          type="index"
          width="80"
          align="align">
        </el-table-column>
        <el-table-column
          label="标题"
          prop="title">
        </el-table-column>
        <el-table-column
          label="优先级"
          prop="priority">
          <div slot-scope="scope">
            <el-tag effect="dark" v-if="scope.row.priority==='紧急'" type="danger" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.priority==='高'" type="warning" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.priority==='中'" type="success" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.priority }}</el-tag>
          </div>
        </el-table-column>
        <el-table-column
          label="迭代"
          prop="iteration">
        </el-table-column>
        <el-table-column
          label="状态"
          prop="state">
          <template slot-scope="scope">
            <el-select v-model="scope.row.state" @change="stateChange(scope.row.id,scope.row.state)" size="small">
              <el-option v-for="item in stateOption" :key="item.value" :value="item.value" :label="item.label"></el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          label="处理人"
          prop="handler">
        </el-table-column>
        <el-table-column
          label="预计开始"
          prop="start">
        </el-table-column>
        <el-table-column
          label="预计结束"
          prop="end">
        </el-table-column>
        <el-table-column
          label="操作">
          <div slot-scope="scope">
            <el-button size="small" type="warning" @click="dialogVisible=true;editOrAdd='edit';getEditRequirementForm(scope.row.id)">详情</el-button>
            <el-button v-if="$cookies.get('user_type')==='管理员'" size="small" type="danger" @click="delRequirement(scope.row.id)">删除</el-button>
            <el-button v-if="$cookies.get('user_type')==='管理员'" style="margin-top: 5px" size="small" type="primary" @click="showLinkVisible=true;searchId=scope.row.id">查看绑定的用例</el-button>
          </div>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
  <RequirementAdd :vs="dialogVisible" :ea="editOrAdd" :editForm="editForm" @getVs="getVs" @fresh="fresh"></RequirementAdd>
  <ShowLinkData :vs="showLinkVisible" :type="'requirement'" :searchId="searchId" @getShowLinkVs="getShowLinkVs"></ShowLinkData>
</div>
</template>

<style scoped>
.el-table {
  display: flex;
  flex-direction: column;
}
</style>
