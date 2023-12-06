<script>
export default {
  props:['document_type','projectId'],
  data() {
    return {
      uploadData:{
        pid:'',
        creator:'',
        document_type:this.document_type,
      },
    };
  },
  mounted() {
  },
  methods:{
    onBeforeUpload(file) {
      if (this.document_type==='项目文档') {
        if (this.projectId) {
          this.uploadData.pid = this.projectId
        }
      }else {
        this.uploadData.pid = -1
      }
      this.uploadData.creator = this.$cookies.get('username')
      const allowSize = file.size / 1024 / 1024 < 10
      if (!allowSize) {
        this.$message.error('文件大小不能超过10MB')
      }
      return allowSize
    },
    onSuccessUpload() {
      location.reload()
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
    :limit="1"
    :before-upload="onBeforeUpload"
    :on-success="onSuccessUpload"
    >
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    <div class="el-upload__tip" slot="tip">只能上传doc/docx/xls/xlsx/txt/pdf/ppt/pptx文件，且文件大小不超过10MB</div>
  </el-upload>
</div>
</template>

<style scoped>

</style>
