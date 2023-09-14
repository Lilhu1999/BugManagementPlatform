<script>
  export default {
    methods: {
      goBack() {
        window.history.back()
      }
    }
  }
</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <el-page-header @back="goBack" content="人员管理">
      </el-page-header>
    </div>
  </el-card>
</div>
</template>

<style scoped>

</style>
