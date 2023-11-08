<script>

</script>

<template>
<div>
  <div>
    <el-form inline>
      <el-form-item label="文件名:">
        <el-input size="small" placeholder="请输入文件名"></el-input>
      </el-form-item>
      <el-form-item label="上传人:">
        <el-input size="small" placeholder="请输入上传人"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button size="small" type="primary">查询</el-button>
        <el-button size="small" type="warning">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
  <el-card>
    <div slot="header">
      <div>
        <el-button size="small" type="success">上传文档</el-button>
        <el-button size="small" type="warning">批量下载</el-button>
      </div>
    </div>
    <div>
      <el-table>
        <el-table-column type="selection" width="50"></el-table-column>
        <el-table-column type="index" label="#" width="50"></el-table-column>
        <el-table-column label="文件名" prop="file_name"></el-table-column>
        <el-table-column label="上传人" prop="creator"></el-table-column>
        <el-table-column label="上传时间" prop="create_time"></el-table-column>
        <el-table-column label="操作">
          <div slot-scope="scope">
            <el-button size="small">下载</el-button>
            <el-button v-if="$cookies.get('user_type')==='管理员'" size="small">删除</el-button>
          </div>
        </el-table-column>
      </el-table>
    </div>
  </el-card>
</div>
</template>

<style scoped>

</style>
