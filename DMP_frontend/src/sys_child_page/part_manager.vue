<script>
import SelectTree from './SelectTree.vue'
  export default {
    components: {SelectTree},
    data() {
      return {
        tableData:[],
        treeData: [],
        empSearchInput:'',
        options:[{
          value:0,
          label:'普通成员'
        },{
          value:1,
          label:'管理员'
        }],
        partDialogVisible:false,
        empDialogVisible:false,
        defaultProps: {
          children: 'children',
          label: 'name'
        },
        addEmpForm:{
          name: '',
          password:'',
          type:'',
          deptId:[],
        },
        addDeptForm:{
          name:'',
          id:[],
        }
      };
    },
    mounted() {
      this.getTreeData()
      this.getEmp()
    },
    methods: {
      goBack() {
        window.history.back()
      },
      // 接收子组件传值
      getPid(pid){
        if (this.partDialogVisible) {
          this.addDeptForm.id=pid
        }else if(this.empDialogVisible){
          this.addEmpForm.deptId=pid
        }
      },
      // 获取部门树
      getTreeData() {
        this.$axios.post('api/getTree/',{
          params:{}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000'){
            this.treeData = res['list']
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      },
      // 新增部门
      addDept() {
        this.$axios.post('api/dept/add/',{
          form:this.addDeptForm
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000'){
            this.$message.success('新增部门成功')
            this.getTreeData()
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      },
      // 新增部门人员
      addEmp() {
        this.$axios.post('api/emp/add/',{
          form:this.addEmpForm
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000'){
            this.$message.success('新增人员成功')
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      },
      // 删除部门人员
      delEmp(id) {
        this.$axios.delete('api/emp/del/',{
          params:{id:id}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000'){
            this.$message.success('删除成功')
            this.getEmp(id)
          }else {
            this.$message.success(res['respMsg'])
          }
        })
      },
      getEmp(id) {
        this.$axios.get('api/emp/info/',{
          params:{id:id,name:this.empSearchInput}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.tableData = res['list']
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      },
      //树节点点击，查询对应部门人员
      handleNodeClick(data, node) {
        console.log("点击节点", data, node);
        this.getEmp(data['id'])
      },
      clearDeptDialog() {
        this.addDeptForm.name=''
        this.addDeptForm.id=[]
      },
      clearEmpDialog() {
        this.addEmpForm.name=''
        this.addEmpForm.password=''
        this.addEmpForm.type=''
        this.addEmpForm.deptId=[]
      },
    }
  }
</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <el-page-header @back="goBack" content="组织架构">
      </el-page-header>
    </div>
    <el-row>
      <el-col :span="6">
        <el-card shadow="never">
          <div slot="header" class="clearfix">
            <el-input placeholder="请输入部门名称" style="width: 150px" size="small"></el-input>
            <el-button size="small" type="primary">查询</el-button>
            <el-button size="small" type="success" @click="partDialogVisible=true">新增</el-button>
          </div>
          <div>
            <el-tree :data="treeData" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
          </div>
        </el-card>
      </el-col>
      <el-col :span="18">
        <el-card shadow="never">
          <div slot="header" class="clearfix">
            <el-input placeholder="请输入员工姓名" style="width: 200px" size="small" v-model="empSearchInput"></el-input>
            <el-button size="small" type="success" style="float: right" @click="empDialogVisible=true">新增</el-button>
          </div>
          <el-table :data="tableData" max-height="95vh" border>
            <el-table-column
              type="index"
              label="#"
              width="50px"
              align="center"
            >
            </el-table-column>
            <el-table-column
              prop="name"
              label="人员姓名"
            >
            </el-table-column>
            <el-table-column
              prop="type"
              label="人员身份"
            >
              <template slot-scope="scope">
                <span v-if="scope.row.type===0">普通用户</span>
                <span v-else-if="scope.row.type===1">管理员</span>
              </template>
            </el-table-column>
            <el-table-column
              label="操作"
            >
              <template slot-scope="scope">
                <el-button type="danger" size="small" @click="delEmp(scope.row.id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </el-card>
  <el-dialog :visible.sync="partDialogVisible" destroy-on-close @close="clearDeptDialog">
    <el-form inline>
      <el-form-item label="部门名称">
        <el-input size="small" v-model="addDeptForm.name"></el-input>
      </el-form-item>
      <el-form-item label="所属部门">
        <SelectTree @getPid="getPid"></SelectTree>
      </el-form-item>
      <el-form-item>
        <div style="float: right">
          <el-button type="primary" size="small" @click="addDept();partDialogVisible=false">
            保存
          </el-button>
          <el-button size="small" @click="partDialogVisible=false">
            取消
          </el-button>
        </div>
      </el-form-item>
    </el-form>
  </el-dialog>
  <el-dialog :visible.sync="empDialogVisible" destroy-on-close @close="clearEmpDialog">
    <el-form inline>
      <el-row>
        <el-col :span="12">
          <el-form-item label="员工姓名">
            <el-input size="small" v-model="addEmpForm.name"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="人员密码">
            <el-input size="small" v-model="addEmpForm.password" show-password></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="所属部门">
            <SelectTree @getPid="getPid"></SelectTree>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="人员身份">
            <el-select v-model="addEmpForm.type" size="small">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="24">
          <el-form-item>
            <div>
              <el-button type="primary" size="small" @click="addEmp();empDialogVisible=false">
                保存
              </el-button>
              <el-button size="small" @click="empDialogVisible=false">
                取消
              </el-button>
            </div>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
  </el-dialog>
</div>
</template>

<style scoped>
.el-card{
  height: 95vh;
}
</style>
