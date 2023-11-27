<script>
export default {
  data() {
    return {
      taskList:[],
    }
  }
}
</script>

<template>
  <div>
    <div>
      <el-card>
        <div slot="header">
          <span>我的工作台</span>
        </div>
        <el-row :gutter="30">
          <el-col :span="12">
            <el-card shadow="never" style="height: 73vh">
              <div slot="header">
                <span>待处理BUG</span>
              </div>
              <div>
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
                </el-table>
              </div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card shadow="never" style="height: 35vh;margin-bottom: 20px">
              <div slot="header">
                <span>参与项目</span>
              </div>
            </el-card>
            <el-card shadow="never" style="height: 35vh">
              <div slot="header">
                <span>消息列表</span>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </div>
</template>

<style scoped>

</style>
