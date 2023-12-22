<script>
  export default {
    data() {
      return {
        filterText:'',
        departmentData:[],
        defaultProps: {
          children: 'children',
          label: 'name',
        },
      }
    },
    watch:{
      filterText(newValue) {
        this.$refs.tree.filter(newValue)
      }
    },
    methods: {
      filterNode(value, data) {
        if (!value) return true;
        return data.label.indexOf(value) !== -1;
      },
    },
  }
</script>

<template>
<div>
  <el-input
    placeholder="输入关键字进行过滤"
    v-model="filterText">
  </el-input>

  <el-tree
    class="filter-tree"
    :data="departmentData"
    :props="defaultProps"
    :filter-node-method="filterNode"
    ref="tree">
  </el-tree>
</div>
</template>

<style scoped>

</style>
