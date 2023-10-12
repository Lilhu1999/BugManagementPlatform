<script>
  import ProjectAddDialog from "../components/dialog/ProjectAddDialog.vue";

  export default {
    components: {ProjectAddDialog},
    data() {
      return {
        tableData:[],
        projectValue:[],
        type:'edit',
        dialogVisible:false,
      }
    },
    mounted() {
      this.getProjectInfo()
    },
    methods: {
      goBack() {
        window.history.back()
      },
      getVisible(val) {
        this.dialogVisible=val
      },
      setVisible() {
        this.dialogVisible = true
      },
      getProjectInfo(id) {
        if (id) {
          this.$axios.get('api/project/info/',{
            params:{id:id}
          }).then((response)=>{
            const res = response.data
            if (res['respCode']==='000000') {
              this.projectValue = res['list'][0]
            }else {
              console.log(res['respMsg'])
            }
          })
        }else {
          this.$axios.get('api/project/info/',{
            params:{status:''}
          }).then((response)=>{
            const res = response.data
            if (res['respCode']==='000000') {
              this.tableData = res['list']
            }else {
              console.log(res['respMsg'])
            }
          })
        }
      },
      delProject(id) {
        this.$confirm('确定删除该项目吗？','删除项目',{
          confirmButtonText:'确认',
          cancelButtonText:'取消',
          type:"warning",
        }).then(()=>{
          this.$axios.delete('api/project/del/',{
            params:{id:id}
          }).then((response)=>{
            const res = response.data
            if (res['respCode']==='000000'){
              this.getProjectInfo()
              this.$message.success('删除成功')
            }else {
              console.log(res['respMsg'])
            }
          })
        }).catch((err)=>{
          this.$message.info('取消删除')
          console.log(err)
        })
      },
    }
  }
</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <el-page-header @back="goBack" content="项目管理">
      </el-page-header>
    </div>
    <div>
      <el-table :data="tableData" max-height="80vh">
        <el-table-column type="index" label="#" width="80px" align="center"></el-table-column>
        <el-table-column prop="name" label="项目名称"></el-table-column>
        <el-table-column prop="desc" label="项目描述"></el-table-column>
        <el-table-column prop="createTime" label="创建时间"></el-table-column>
        <el-table-column prop="status" label="项目状态"></el-table-column>
        <el-table-column label="操作">
          <div slot-scope="scope">
            <el-button type="warning" size="small" @click="getProjectInfo(scope.row.id);setVisible()">修改</el-button>
            <el-button type="danger" size="small" @click="delProject(scope.row.id)">删除</el-button>
          </div>
        </el-table-column>
      </el-table>
    </div>
  </el-card>
  <ProjectAddDialog
    :type="type"
    :vs="dialogVisible"
    :projectValue="projectValue"
    @getVisible="getVisible"
  ></ProjectAddDialog>
</div>
</template>

<style scoped>

</style>
