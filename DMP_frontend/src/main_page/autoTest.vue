<script setup>

import SendRequest from "../views/autoTest/interfaceAutomation/sendRequest.vue";
</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <span>自动化测试平台</span>
    </div>
    <div>
      <el-tabs>
        <el-tab-pane label="接口自动化">
          <div>
            <el-card shadow="never">
              <div>
                <SendRequest></SendRequest>
              </div>
            </el-card>
          </div>
        </el-tab-pane>
        <el-tab-pane label="UI自动化"></el-tab-pane>
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
