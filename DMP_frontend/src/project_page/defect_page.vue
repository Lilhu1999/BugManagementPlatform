<script>
import DefectDialog from "../components/dialog/DefectDialog.vue";
import LinkDialog from "../components/dialog/LinkDialog.vue";
import ShaiXuan from "../components/shaixuan.vue";

export default {
  components: {LinkDialog, DefectDialog,ShaiXuan},
  data(){
    return {
      allData:[],
      tableData: [],
      selectionArr: [],// 被选中的缺陷的数组
      dialogVisible: false,
      linkDialogVisible: false,
      pid: '',
      editOrAdd: '',
      editForm: [],
      selectValue: '',
      option: [{
        value: '待解决',
        label: '待解决'
      }, {
        value: '已解决',
        label: '已解决'
      }, {
        value: '重新打开',
        label: '重新打开'
      }, {
        value: '已关闭',
        label: '已关闭'
      }],
    }
  },
  created() {
    this.pid = sessionStorage.getItem('pid')
    this.getDefectInfo(this.pid)
  },
  methods:{
    // 父组件接收到子组件val时，关闭dialog
    getVs(val) {
      this.dialogVisible=val
    },
    getLinkDialogVs(val) {
      this.linkDialogVisible =val
    },
    getSelectedData(val) {
      let arr = this.allData
      let temp = []
      let arr_id = []
      for (let i in val) {
        if (val[i] !== '全部') {
          for (let j in arr) {
            if (arr[j][i] === val[i]) {
              if (arr_id.includes(arr[j]['id'])) {
                continue
              }else {
                arr_id.push(arr[j]['id'])
                temp.push(arr[j])
              }
            }
          }
          arr = temp
        }
      }
      this.tableData = arr
    },
    // 父组件接收到子组件传递的val时，触发搜索页面数据操作
    fresh(val){
      if (val) {
        this.getDefectInfo(this.pid)
      }
    },
    // 通过session内存储的项目ID获取缺陷列表
    getDefectInfo(pid) {
      this.$axios.get('api/project/defect/info/',{
        params:{pid:pid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000'){
          this.allData = res['list']
          this.tableData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 点击详情查询目标缺陷内容
    getEditDefectForm(rid) {
      this.$axios.get('api/project/defect/info/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000'){
          this.editForm = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 缺陷删除按钮
    delDefect(rid) {
      this.$axios.get('api/project/defect/del/',{
        params:{rid:rid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('删除成功')
          this.getDefectInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 更新缺陷状态
    stateChange(rid,newState) {
      this.$axios.post('api/project/defect/updateState/',{
        rid:rid,newState:newState
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.getDefectInfo(this.pid)
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 更多操作下拉框功能
    dropdownCommand(command) {
      if (command==='link') {
        if (this.selectionArr[0]) {
          this.linkDialogVisible=true
        }else {
          this.$message.info('请勾选需要进行绑定操作的缺陷')
        }
      }
    },
    selectionChange(selection)  {
      this.selectionArr = selection
    },
    // 根据缺陷状态动态更换css
    tableRowClassName({row, rowIndex}) {
      if (row['state']==='已解决') {
        return 'success-row'
      }else if (row['state']==='待解决') {
        return 'error-row'
      }else if (row['state']==='重新打开') {
        return 'warning-row'
      }
      return ''
    },
  },
}
</script>

<template>
<div>
  <div style="margin-bottom: 10px">
    <el-button
      type="primary"
      size="small"
      icon="el-icon-circle-plus-outline"
      @click="dialogVisible=true;editOrAdd='add'"
      >
      创建缺陷
    </el-button>
    <el-dropdown @command="dropdownCommand">
      <el-button type="primary" plain size="small">更多操作<i class="el-icon-arrow-down el-icon--right"></i></el-button>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-upload2">导入缺陷</el-dropdown-item>
        <el-dropdown-item icon="el-icon-download">导出缺陷</el-dropdown-item>
        <el-dropdown-item icon="el-icon-link" command="link">关联用例</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <ShaiXuan style="float: right" @getSelectedData="getSelectedData"></ShaiXuan>
  </div>
  <div>
    <el-card>
      <el-table :row-class-name="tableRowClassName" :data="tableData" max-height="70vh" style="width: 100%;min-height: 65vh" @selection-change="selectionChange">
        <el-table-column
          type="selection"
          width="50">
        </el-table-column>
        <el-table-column
          label="#"
          type="index"
          width="50"
          align="align">
        </el-table-column>
        <el-table-column
          label="标题"
          prop="title"
          width="300">
        </el-table-column>
        <el-table-column
          label="优先级"
          prop="priority">
          <div slot-scope="scope">
            <el-tag effect="dark" v-if="scope.row.priority==='紧急'" type="danger" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.priority==='高'" type="warning" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.priority==='中'" type="success" size="small">{{ scope.row.priority }}</el-tag>
            <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.priority }}</el-tag>
          </div>
        </el-table-column>
        <el-table-column
          label="严重程度"
          prop="importance">
          <div slot-scope="scope">
            <el-tag effect="dark" v-if="scope.row.importance==='致命'" type="danger" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.importance==='严重'" type="warning" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else-if="scope.row.importance==='一般'" type="success" size="small">{{ scope.row.importance }}</el-tag>
            <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.importance }}</el-tag>
          </div>
        </el-table-column>
        <el-table-column
          label="迭代"
          prop="iteration">
        </el-table-column>
        <el-table-column
          label="状态"
          prop="state">
          <template slot-scope="scope">
            <el-select v-model="scope.row.state" @change="stateChange(scope.row.id,scope.row.state)" size="small">
              <el-option v-for="item in option" :key="item.value" :value="item.value" :label="item.label"></el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          label="处理人"
          prop="handler">
        </el-table-column>
        <el-table-column
          label="创建人"
          prop="creator">
        </el-table-column>
        <el-table-column
          label="创建时间"
          prop="createTime">
        </el-table-column>
        <el-table-column
          label="操作"
          width="150">
          <div slot-scope="scope">
            <el-button size="small" type="warning" @click="dialogVisible=true;editOrAdd='edit';getEditDefectForm(scope.row.id)">详情</el-button>
            <el-button v-if="$cookies.get('user_type')==='管理员'" size="small" type="danger" @click="delDefect(scope.row.id)">删除</el-button>
          </div>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
  <LinkDialog :vs="linkDialogVisible" :type="'testCase'" :selectionArr="this.selectionArr" @getLinkDialogVs="getLinkDialogVs"></LinkDialog>
  <DefectDialog :vs="dialogVisible" :ea="editOrAdd" :editForm="editForm" @getVs="getVs" @fresh="fresh"></DefectDialog>
</div>
</template>

<style scoped>
.el-table {
  display: flex;
  flex-direction: column;
}
.el-table /deep/ .success-row {
  background: #f7ffe6;
}
.el-table /deep/ .error-row {
  background: #fce9e9;
}
.el-table /deep/ .warning-row {
  background:oldlace;
}
</style>
