<script>
export default {
  props:['vs', 'type', 'selectionArr'],
  data() {
    return {
      tableData:[],
      selection:[],
      pid:'',
      dialogVisible:false,
    }
  },
  mounted() {
    this.getTableData()
  },
  watch:{
    vs(newValue) {
      if (newValue===true) {
        this.dialogVisible=true
      }
    },
    selectionArr(newValue) {
      if (newValue) {
        const arr = []
        for (let key in newValue) {
          arr.push(newValue[key].id)
        }
        this.selection = arr
      }
    }
  },
  methods:{
    setVs() {
      this.$emit('getLinkDialogVs',false)
    },
    async getPid() {
      return sessionStorage.getItem('pid')
    },
    async getTableData() {
      if (this.type==='requirement') {
        let pid = await this.getPid()
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
      }else {
        let pid = await this.getPid()
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
      }
    },
    link(rid) {
      if (this.type==='requirement') {
        this.$axios.post('api/project/testcase/link/',{
          selection:this.selection,rid:rid
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.$message.success('绑定成功')
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      }else {
        this.$axios.post('api/project/defect/link/',{
          selection:this.selection,rid:rid
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.$message.success('绑定成功')
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      }
    },
  },
}
</script>

<template>
<div>
  <el-dialog width="50%" :visible="dialogVisible" @close="dialogVisible=false;setVs()">
    <div slot="title">
      <span v-if="type==='requirement'">绑定需求</span>
      <span v-else>绑定用例</span>
    </div>
    <div slot="footer">
      <el-button size="small" @click="dialogVisible=false;setVs()">退出</el-button>
    </div>
    <el-table max-height="40vh" :data="tableData">
      <el-table-column label="ID" prop="id"></el-table-column>
      <el-table-column label="标题" prop="title"></el-table-column>
      <el-table-column label="操作">
        <div slot-scope="scope">
          <el-button size="small" type="success" @click="dialogVisible=false;setVs();link(scope.row.id)">绑定</el-button>
        </div>
      </el-table-column>
    </el-table>
  </el-dialog>
</div>
</template>

<style scoped>

</style>
