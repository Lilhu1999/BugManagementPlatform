<script>
import DefectDialog from "../components/dialog/DefectDialog.vue";

export default {
  components: {DefectDialog},
  data(){
    return{
      tableData:[],
      dialogVisible:false,
      pid:'',
      editOrAdd:'',
      editForm:[],
      selectValue:'',
      option:[{
        value: '待解决',
        label: '待解决'
      }, {
        value: '已解决',
        label: '已解决'
      }, {
        value: '重新打开',
        label: '重新打开'
      }, {
        value: '已关闭',
        label: '已关闭'
      }]
    }
  },
  created() {
    this.pid = sessionStorage.getItem('pid')
    this.getDefectInfo(this.pid)
  },
  methods:{
    // 父组件接收到子组件val时，关闭dialog
    getVs(val) {
      this.dialogVisible=val
    },
    // 父组件接收到子组件传递的val时，触发搜索页面数据操作
    fresh(val){
      if (val) {
        this.getDefectInfo(this.pid)
      }
    },
    // 通过session内存储的项目ID获取需求列表
    getDefectInfo(pid) {
      this.$axios.get('api/project/defect/info/',{
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
    getEditDefectForm(rid) {
      this.$axios.get('api/project/defect/info/',{
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
    delDefect(rid) {
      this.$axios.get('api/project/defect/del/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('删除成功')
          this.getDefectInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 更新需求状态
    stateChange(rid,newState) {
      this.$axios.post('api/project/defect/updateState/',{
        rid:rid,newState:newState
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.getDefectInfo(this.pid)
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
      创建缺陷
    </el-button>
    <el-dropdown>
      <el-button type="primary" plain size="small">更多操作<i class="el-icon-arrow-down el-icon--right"></i></el-button>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-upload2">导入缺陷</el-dropdown-item>
        <el-dropdown-item icon="el-icon-download">导出缺陷</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
  <div>
    <el-card>
      <el-table :data="tableData" max-height="70vh" style="width: 100%;min-height: 65vh">
        <el-table-column
          label="#"
          type="index"
          width="50"
          align="align">
        </el-table-column>
        <el-table-column
          label="标题"
          prop="title"
          width="300">
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
          label="严重程度"
          prop="importance">
          <div slot-scope="scope">
            <el-tag effect="dark" v-if="scope.row.importance==='致命'" type="danger" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.importance==='严重'" type="warning" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.importance==='一般'" type="success" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.importance }}</el-tag>
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
              <el-option v-for="item in option" :key="item.value" :value="item.value" :label="item.label"></el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          label="处理人"
          prop="handler">
        </el-table-column>
        <el-table-column
          label="创建人"
          prop="creator">
        </el-table-column>
        <el-table-column
          label="创建时间"
          prop="createTime">
        </el-table-column>
        <el-table-column
          label="操作"
          width="150">
          <div slot-scope="scope">
            <el-button size="small" type="warning" @click="dialogVisible=true;editOrAdd='edit';getEditDefectForm(scope.row.id)">详情</el-button>
            <el-button size="small" type="danger" @click="delDefect(scope.row.id)">删除</el-button>
          </div>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
  <DefectDialog :vs="dialogVisible" :ea="editOrAdd" :editForm="editForm" @getVs="getVs" @fresh="fresh"></DefectDialog>
</div>
</template>

<style scoped>
.el-table {
  display: flex;
  flex-direction: column;
}
</style>
