<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1>🔐 Personal Insights</h1>
        <el-menu mode="horizontal" :router="true" :default-active="$route.path">
          <el-menu-item index="/">📊 总览</el-menu-item>
          <el-menu-item index="/skills">🎯 技能</el-menu-item>
          <el-menu-item index="/timeline">📅 时间线</el-menu-item>
          <el-menu-item index="/health">🏥 健康</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
// App component
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
}

.el-header {
  background-color: #409EFF;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
}

.el-header h1 {
  margin-right: 40px;
  font-size: 24px;
}

.el-menu {
  background-color: transparent;
  border: none;
  flex: 1;
}

.el-menu-item {
  color: white !important;
}

.el-menu-item.is-active {
  background-color: rgba(255, 255, 255, 0.2) !important;
}

.el-main {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: calc(100vh - 60px);
}
</style>
