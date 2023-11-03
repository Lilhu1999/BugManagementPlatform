<script>
export default {
  props:['vs', 'type', 'searchId'],
  data() {
    return {
      dialogVisible:false,
      tableData:[],
    }
  },
  watch:{
    vs(newValue) {
      if (newValue) {
        this.dialogVisible=newValue
      }
    },
    searchId(newValue) {
      if (newValue) {
        this.setTableData(newValue)
      }
    }
  },
  methods:{
    // 获取table数据
    setTableData(linkId) {
      if (this.type==='requirement') {
        this.$axios.get('api/project/testcase/info/',{
          params:{linkId:linkId}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.tableData = res['list']
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      }else {
        this.$axios.get('api/project/defect/info/',{
          params:{linkId:linkId}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000') {
            this.tableData = res['list']
          }else {
            this.$message.error(res['respMsg'])
          }
        })
      }
    },
    setShowLinkVs() {
      this.$emit('getShowLinkVs',false)
    }
  },
}
</script>

<template>
<div>
  <el-dialog :visible="dialogVisible" width="100%" @close="dialogVisible=false;setShowLinkVs()">
    <div slot="title">
      <span>查看绑定数据</span>
    </div>
    <div slot="footer">
      <el-button size="small" type="primary" @click="dialogVisible=false;setShowLinkVs()">返回</el-button>
    </div>
    <div v-if="type==='requirement'">
      <el-table :data="tableData">
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
          <div slot-scope="scope">
            <el-tag effect="dark" v-if="scope.row.level==='高'" type="danger" size="small">{{ scope.row.level }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.level==='中'" type="success" size="small">{{ scope.row.level }}</el-tag>
            <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.level }}</el-tag>
          </div>
        </el-table-column>
        <el-table-column
          label="用例状态"
          prop="state">
        </el-table-column>
        <el-table-column
          label="创建人"
          prop="creator">
        </el-table-column>
        <el-table-column
          label="创建时间"
          prop="createTime">
        </el-table-column>
      </el-table>
    </div>
    <div v-if="type==='testCase'">
      <el-table :data="tableData">
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
      </el-table>
    </div>
  </el-dialog>
</div>
</template>

<style scoped>

</style>
