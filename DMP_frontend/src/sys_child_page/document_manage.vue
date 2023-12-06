<script>

import Upload from "../components/upload.vue";

export default {
  components: {Upload},
  data() {
    return {
      dialogVisible:false,
      active:0,
      tableData:[],
      documentOptions: [{
          value: '公共文档',
          label: '公共文档'
        }, {
          value: '项目文档',
          label: '项目文档'
        }],
      projectOptions:[],
      projectValue: '',
      onProject:'',
      document_type: '',
    }
  },
  watch: {
    document_type(newValue) {
      if (newValue==='公共文档') {
        this.next()
      }else {
        this.onProject = '项目文档'
      }
    },
    projectValue(newValue) {
      if (newValue) {
        this.next()
      }
    }
  },
  mounted() {
    this.getTableData()
    this.getProjectData()
  },
  methods: {
    // 获取页面数据
    getTableData() {
      this.$axios.get('api/project/document/info/', {
        params: {
          pid: '-1',
        }
      }).then((response) => {
        const res = response.data
        if (res['respCode'] === '000000') {
          this.tableData = res['list']
        } else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 获取项目数据
    getProjectData() {
      this.$axios.get('api/project/info/',
      ).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.projectOptions = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 单文件下载
    download(uid, name) {
      this.$axios({
        method: 'get',
        url: 'api/download/',
        params: {
          uid: uid,
        },
        responseType: "blob"
      }).then((response) => {
        const res = response.data
        const url = window.URL.createObjectURL(new Blob([res]));
        const link = document.createElement('a');
        link.href = url
        link.setAttribute('download', name);
        document.body.appendChild(link);
        link.click()
      }).catch((e) => {
        console.log(e)
      })
    },
    // 删除文件
    delFile(uid) {
      this.$confirm('确定删除该文件吗？', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: "warning"
      })
        .then(() => {
          this.$axios.delete('api/project/document/del/', {
            params: {uid: uid}
          }).then((response) => {
            const res = response.data
            if (res['respCode'] === '000000') {
              this.$message.success('删除成功')
              this.getTableData()
            } else {
              this.$message.error(res['respMsg'])
            }
          })
        })
        .catch(() => {
          this.$message.info('取消删除')
        })
    },
    next() {
        if (this.active++ > 1) this.active = 0;
      },
    clear() {
      this.$nextTick(()=>{
        this.active=0
        this.value=''
      })
    },
    goBack() {
        window.history.back()
    },
  }
}
</script>

<template>
  <div>
    <div>
      <el-card>
        <div slot="header">
          <el-page-header @back="goBack" content="文档管理">
          </el-page-header>
        </div>
        <div>
          <div>
            <el-button size="small" type="success" @click="dialogVisible=true">上传文档</el-button>
            <el-button size="small" type="warning">批量下载</el-button>
          </div>
          <el-table :data="tableData">
            <el-table-column type="selection" width="50"></el-table-column>
            <el-table-column type="index" label="#" width="50"></el-table-column>
            <el-table-column label="文件名" prop="fileName"></el-table-column>
            <el-table-column label="上传人" prop="creator"></el-table-column>
            <el-table-column label="文件类型" prop="document_type"></el-table-column>
            <el-table-column label="上传时间" prop="createTime"></el-table-column>
            <el-table-column label="操作">
              <div slot-scope="scope">
                <el-button size="small" type="primary" @click="download(scope.row.id,scope.row.fileName)">下载</el-button>
                <el-button v-if="$cookies.get('user_type')==='管理员'" size="small" type="danger" @click="delFile(scope.row.id)">删除</el-button>
              </div>
            </el-table-column>
          </el-table>
        </div>
      </el-card>
    </div>
    <div>
      <el-dialog :visible="dialogVisible" width="40wh" @close="dialogVisible=false;getTableData();clear()">
        <div slot="title">上传文档</div>
        <el-row>
          <el-col :span="16">
            <div v-if="active===1">
              <Upload :document_type="document_type" :projectId="projectValue"></Upload>
            </div>
            <div v-if="active===0">
              <el-select v-model="document_type" placeholder="请选择文件类型">
                <el-option
                  v-for="item in documentOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
            <div v-if="active===0 && onProject==='项目文档'" style="margin-top: 20px">
              <el-select v-model="projectValue" placeholder="请选择所属项目">
                <el-option
                  v-for="item in projectOptions"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id">
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="8">
            <div style="height: 200px">
              <el-steps :active="active" finish-status="success" direction="vertical">
                <el-step title="选择文件类型"></el-step>
                <el-step title="上传文件"></el-step>
              </el-steps>
            </div>
          </el-col>
        </el-row>
      </el-dialog>
    </div>
  </div>
</template>

<style scoped>

</style>
