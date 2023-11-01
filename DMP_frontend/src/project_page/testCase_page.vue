<script>
import TestCaseDialog from "../components/dialog/TestCaseDialog.vue";

export default {
  components: {TestCaseDialog},
  data(){
    return{
      tableData:[],
      dialogVisible:false,
      pid:'',
      editOrAdd:'',
      editForm:[],
      selectValue:'',
      option:[
        {
        value: '正常',
        label: '正常'
      },{
        value: '通过',
        label: '通过'
      }, {
        value: '不通过',
        label: '不通过'
      }, {
        value: '延期',
        label: '延期'
      }]
    }
  },
  created() {
    this.pid = sessionStorage.getItem('pid')
    this.getTestCaseInfo(this.pid)
  },
  methods:{
    // 父组件接收到子组件val时，关闭dialog
    getVs(val) {
      this.dialogVisible=val
    },
    // 父组件接收到子组件传递的val时，触发搜索页面数据操作
    fresh(val){
      if (val) {
        this.getTestCaseInfo(this.pid)
      }
    },
    // 通过session内存储的项目ID获取需求列表
    getTestCaseInfo(pid) {
      this.$axios.get('api/project/testcase/info/',{
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
    getEditTestCaseForm(rid) {
      this.$axios.get('api/project/testcase/info/',{
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
    delTestCase(rid) {
      this.$axios.get('api/project/testcase/del/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('删除成功')
          this.getTestCaseInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 更新需求状态
    stateChange(rid,newState) {
      this.$axios.post('api/project/testcase/updateState/',{
        rid:rid,newState:newState
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.getTestCaseInfo(this.pid)
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
      创建用例
    </el-button>
    <el-dropdown>
      <el-button type="primary" plain size="small">更多操作<i class="el-icon-arrow-down el-icon--right"></i></el-button>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-upload2">导入用例</el-dropdown-item>
        <el-dropdown-item icon="el-icon-download">导出用例</el-dropdown-item>
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
          label="用例类型"
          prop="type">
        </el-table-column>
        <el-table-column
          label="用例等级"
          prop="level">
        </el-table-column>
        <el-table-column
          label="用例状态"
          prop="state">
          <template slot-scope="scope">
            <el-select v-model="scope.row.state" @change="stateChange(scope.row.id,scope.row.state)" size="small">
              <el-option v-for="item in option" :key="item.value" :value="item.value" :label="item.label"></el-option>
            </el-select>
          </template>
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
            <el-button size="small" type="warning" @click="dialogVisible=true;editOrAdd='edit';getEditTestCaseForm(scope.row.id)">详情</el-button>
            <el-button size="small" type="danger" @click="delTestCase(scope.row.id)">删除</el-button>
          </div>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
  <TestCaseDialog :vs="dialogVisible" :ea="editOrAdd" :editForm="editForm" @getVs="getVs" @fresh="fresh"></TestCaseDialog>
</div>
</template>

<style scoped>
.el-table {
  display: flex;
  flex-direction: column;
}
</style>
