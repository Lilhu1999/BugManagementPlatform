<script setup>

</script>

<template>
<div>
  <el-card shadow="never">
    <div slot="header">
      <span>系统设置</span>
    </div>
    <el-row :gutter="30">
      <el-col :span="4">
        <div class="div_img" @click="$router.push('projectManager')">
          <div>
            <el-image :src="require('../assets/系统设置页面人员管理图标.png')"></el-image>
          </div>
          <div>
            <span>项目管理</span>
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="div_img" @click="$router.push('partManager')">
          <div>
            <el-image :src="require('../assets/系统设置页面部门管理图标.png')"></el-image>
          </div>
          <div>
            <span>组织架构</span>
          </div>
        </div>
      </el-col>
    </el-row>
  </el-card>
  <router-view></router-view>
</div>
</template>

<style scoped>
.div_img {
  text-align: center;
  padding: 20px;
  cursor: pointer;
}
</style>
