<script>
export default {
  data() {
    return{
      allIterationData:[],
    }
  }
}
</script>

<template>
  <div>
    <el-row :gutter="10">
      <el-col :span="6">
        <el-card shadow="never" style="height: 75vh">
          <div slot="header">
            <el-button size="small" type="text" icon="el-icon-circle-plus-outline">创建迭代</el-button>
          </div>
          <div v-for="item in allIterationData">
            <el-card shadow="never"></el-card>
          </div>
        </el-card>
      </el-col>
      <el-col :span="18">
        <div style="margin-bottom: 12px">
          <el-card shadow="never"></el-card>
        </div>
        <div>
          <el-card shadow="never" style="height: 68vh"></el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.el-button--text {
  color: #999999;
}
</style>
