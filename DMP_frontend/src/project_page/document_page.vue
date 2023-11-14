<script>
import Upload from "../components/upload.vue";
export default {
  components: {Upload},
  data() {
    return {
      dialogVisible:false,
      tableData:[],
      searchForm:{
        fileName:'',
        creator:'',
      },
    };
  },
  mounted() {
    this.getTableData()
  },
  methods:{
    // 获取页面数据
    getTableData() {
      this.$axios.get('api/project/document/info/',{
        params:{pid:sessionStorage.getItem('pid'),fileName:this.searchForm.fileName,creator:this.searchForm.creator}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.tableData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 单文件下载
    download(uid, name) {
      this.$axios({
        method:'get',
        url:'api/download/',
        params:{
          uid:uid,
        },
        responseType:"blob"
      }).then((response)=>{
        const res = response.data
        const url = window.URL.createObjectURL(new Blob([res]));
        const link = document.createElement('a');
        link.href = url
        link.setAttribute('download', name);
        document.body.appendChild(link);
        link.click()
      }).catch((e)=>{
          console.log(e)
        })
    },
    // 删除文件
    delFile(uid) {
      this.$confirm('确定删除该文件吗？',{
        confirmButtonText:'确定',
        cancelButtonText:'取消',
        type:"warning"
      })
        .then(()=>{
          this.$axios.delete('api/project/document/del/', {
          params:{uid:uid}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.$message.success('删除成功')
            this.getTableData()
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      })
        .catch(()=>{
          this.$message.info('取消删除')
        })
    },
  }
}
</script>

<template>
<div>
  <div>
    <el-form inline>
      <el-form-item label="文件名:">
        <el-input size="small" placeholder="请输入文件名" v-model="searchForm.fileName"></el-input>
      </el-form-item>
      <el-form-item label="上传人:">
        <el-input size="small" placeholder="请输入上传人" v-model="searchForm.creator"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button size="small" type="primary" @click="getTableData">查询</el-button>
        <el-button size="small" type="warning">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
  <div>
    <el-card>
      <div slot="header">
        <div>
          <el-button size="small" type="success" @click="dialogVisible=true">上传文档</el-button>
          <el-button size="small" type="warning">批量下载</el-button>
        </div>
      </div>
      <div>
        <el-table :data="tableData">
          <el-table-column type="selection" width="50"></el-table-column>
          <el-table-column type="index" label="#" width="50"></el-table-column>
          <el-table-column label="文件名" prop="fileName"></el-table-column>
          <el-table-column label="上传人" prop="creator"></el-table-column>
          <el-table-column label="上传时间" prop="createTime"></el-table-column>
          <el-table-column label="操作">
            <div slot-scope="scope">
              <el-button size="small" type="primary" @click="download(scope.row.id,scope.row.fileName)">下载</el-button>
              <el-button v-if="$cookies.get('user_type')==='管理员'" size="small" type="danger" @click="delFile(scope.row.id)">删除</el-button>
            </div>
          </el-table-column>
        </el-table>
      </div>
    </el-card>
  </div>
  <div>
    <el-dialog :visible="dialogVisible" width="400px" @close="dialogVisible=false;getTableData()">
      <div slot="title">上传项目文档</div>
      <div>
        <Upload></Upload>
      </div>
    </el-dialog>
  </div>
</div>
</template>

<style scoped>

</style>
