<script>
export default {
  props:['pid', 'creator'],
  data() {
    return {
      data:[this.pid, this.creator],
    };
  },
}
</script>

<template>
<div>
  <el-upload
    class="upload-demo"
    accept="doc,docx,xls,xlsx,txt,pdf,ppt,pptx"
    :data="data"
    drag
    action="api/upload/"
    multiple>
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    <div class="el-upload__tip" slot="tip">只能上传doc/docx/xls/xlsx/txt/pdf/ppt/pptx文件，且文件大小不超过10MB</div>
  </el-upload>x
</div>
</template>

<style scoped>

</style>
