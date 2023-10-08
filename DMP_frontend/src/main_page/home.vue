<script>

</script>

<template>
  <div>
    <div>
      <el-card>
        <div slot="header">
          <span>我的工作台</span>
        </div>
        <el-row :gutter="30">
          <el-col :span="12">
            <el-card shadow="never" style="height: 83vh">
              <div slot="header">
                <span>任务列表</span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="never" style="height: 40vh;margin-bottom: 20px">
              <div slot="header">
                <span>参与项目</span>
              </div>
            </el-card>
            <el-card shadow="never" style="height: 40vh">
              <div slot="header">
                <span>消息列表</span>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </div>
</template>

<style scoped>

</style>
