<script >
export default {
  data() {
    return {
      select:'',
      address:'',
    }
  },
}
</script>

<template>
  <div>
    <el-input placeholder="请输入内容" v-model="address" class="input-with-select">
      <el-select v-model="select" slot="prepend" placeholder="请选择">
        <el-option label="POST" value="1"></el-option>
        <el-option label="GET" value="2"></el-option>
        <el-option label="PUT" value="3"></el-option>
        <el-option label="DELETE" value="3"></el-option>
        <el-option label="OPTIONS" value="3"></el-option>
      </el-select>
      <el-button slot="append">发送</el-button>
    </el-input>
  </div>
</template>

<style scoped>

</style>
