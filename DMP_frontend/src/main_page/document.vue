<script>
export default {
  data() {
    return {
      fileData:[],
      active_type:'公共文档',
    }
  },
  mounted() {
    this.getFileData()
  },
  methods: {
    // 获取文件数据
    getFileData() {
      this.$axios.get('api/public/document/info/',{
        params:{document_type:this.active_type}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.fileData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 单文件下载
    download(uid, name) {
      this.$axios({
        method:'get',
        url:'api/download/',
        params:{
          uid:uid,
        },
        responseType:"blob"
      }).then((response)=>{
        const res = response.data
        const url = window.URL.createObjectURL(new Blob([res]));
        const link = document.createElement('a');
        link.href = url
        link.setAttribute('download', name);
        document.body.appendChild(link);
        link.click()
      }).catch((e)=>{
          console.log(e)
        })
    },
    tabClick() {
      this.getFileData()
    }
  },
}
</script>

<template>
<div>
  <el-card>
    <div>
      <el-tabs v-model="active_type" @tab-click="tabClick">
        <el-tab-pane label="公共文档" name="公共文档">
          <el-row :gutter="30">
            <el-col :span="2" v-for="item in fileData" :key="item.id" @click.native="download(item.id, item.fileName)">
              <div class="file_div">
                <div>
                  <el-image :src="require('../assets/fileicon/'+ item.fileName.split('.')[1] +'-icon.png')"></el-image>
                </div>
                <div>
                  <span class="file_title">{{ item.fileName }}</span>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="项目文档" name="项目文档">
          <el-row :gutter="30">
            <el-col :span="2" v-for="item in fileData" :key="item.id" @click.native="download(item.id, item.fileName)">
              <div class="file_div">
                <div>
                  <el-image :src="require('../assets/fileicon/'+ item.fileName.split('.')[1] +'-icon.png')"></el-image>
                </div>
                <div>
                  <span class="file_title">{{ item.fileName }}</span>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </div>
  </el-card>
</div>
</template>

<style scoped>
.el-card{
  height: 88vh;
}
.file_div {
  display: flex;
  width: 80px;
  height: 120px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  overflow-x: hidden;
  cursor: pointer;
}
.file_title {
  font-size: 10px;
  overflow: hidden;
}
</style>
