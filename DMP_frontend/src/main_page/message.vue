<script setup>

</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <span>消息列表</span>
    </div>
    <div>
      <el-tabs>
        <el-tab-pane label="未读消息">待办</el-tab-pane>
        <el-tab-pane label="已读消息"></el-tab-pane>
      </el-tabs>
    </div>
  </el-card>
</div>
</template>

<style scoped>
.el-card{
  height: 97vh;
}
</style>
