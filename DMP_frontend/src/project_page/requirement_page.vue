<script>
import RequirementAdd from "../components/dialog/RequirementAdd.vue";

export default {
  components: {RequirementAdd},
  data(){
    return{
      tableData:[],
      dialogVisible:false,
    }
  },
  methods:{
    getVs(val) {
      this.dialogVisible=val
    }
  },
}
</script>

<template>
<div>
  <div>
    <el-button
      type="primary"
      size="small"
      icon="el-icon-circle-plus-outline"
      @click="dialogVisible=true"
      style="margin-bottom: 10px">
      创建需求
    </el-button>
  </div>
  <div>
    <el-card>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column
          label="#"
          prop="index"
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
          label="预计开始"
          prop="start">
        </el-table-column>
        <el-table-column
          label="预计结束"
          prop="end">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
  <RequirementAdd :vs="dialogVisible" @getVs="getVs"></RequirementAdd>
</div>
</template>

<style scoped>

</style>
