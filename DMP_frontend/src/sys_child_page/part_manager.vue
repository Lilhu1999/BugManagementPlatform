<script>
  export default {
    data() {
      return {
        data: [{
          label: '一级 1',
          children: [{
            label: '二级 1-1',
            children: [{
              label: '三级 1-1-1'
            }]
          }]
        }, {
          label: '一级 2',
          children: [{
            label: '二级 2-1',
            children: [{
              label: '三级 2-1-1'
            }]
          }, {
            label: '二级 2-2',
            children: [{
              label: '三级 2-2-1'
            }]
          }]
        }, {
          label: '一级 3',
          children: [{
            label: '二级 3-1',
            children: [{
              label: '三级 3-1-1'
            }]
          }, {
            label: '二级 3-2',
            children: [{
              label: '三级 3-2-1'
            }]
          }]
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
      };
    },
    methods: {
      goBack() {
        window.history.back()
      }
    }
  }
</script>

<template>
<div>
  <el-card>
    <div slot="header">
      <el-page-header @back="goBack" content="组织架构">
      </el-page-header>
    </div>
    <el-row :gutter="30">
      <el-col :span="6">
        <div>
          <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
        </div>
      </el-col>
      <el-col :span="18">
        <div>
        </div>
      </el-col>
    </el-row>
  </el-card>
</div>
</template>

<style scoped>

</style>
