<script>
export default {
  data() {
    return {
      uploadData:{
        pid:'',
        creator:'',
      },
    };
  },
  mounted() {
  },
  methods:{
    onBeforeUpload(file) {
      this.uploadData.pid = sessionStorage.getItem('pid')
      this.uploadData.creator = this.$cookies.get('username')
      const allowSize = file.size / 1024 / 1024 < 10
      if (!allowSize) {
        this.$message.error('文件大小不能超过10MB')
      }
      return allowSize
    },
  },
}
</script>

<template>
<div>
  <el-upload
    class="upload-demo"
    accept=".doc,.docx,.xls,.xlsx,.txt,.pdf,.ppt,.pptx"
    :data="uploadData"
    drag
    :show-file-list="false"
    action="api/upload/"
    multiple
    :limit="5"
    :before-upload="onBeforeUpload"
    >
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    <div class="el-upload__tip" slot="tip">只能上传doc/docx/xls/xlsx/txt/pdf/ppt/pptx文件，且文件大小不超过10MB</div>
  </el-upload>
</div>
</template>

<style scoped>

</style>
