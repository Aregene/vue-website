<!--
 * @Date: 2025-02-14 10:52:42
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-17 13:28:23
-->

<!--  SportDisplay.vue  ---->

<template>
  <div class="project-showcase">
    <h2 class="title">Our practical achievements</h2>
    <p class="description">
      We took photos and visited the Wanfo Pavilion to gain a deep understanding of the ancient brick culture
    </p>
    <div class="images">
      <div class="image-container">
        <img :src="image1" alt="Project 1" />
        <p class="image-caption">ELEMENTARY COFFEE CO.</p>
      </div>
      <div class="image-container">
        <img :src="image2" alt="Project 2" />
        <p class="image-caption">NEXT STEP PERFORMANCE</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectShowcase",
  data() {
    return {
      image1: require('@/assets/wall.jpg'),
      image2: require('@/assets/post.jpg'),
    };
  },
};
</script>

<style scoped>
.project-showcase {
  text-align: center;
  background-color: #8A8A8A;
  color: white;
  padding: 20px;
  font-family: "Georgia", serif; /* 使用类衬线字体 */
}

.title {
  font-size: 14px;
  font-weight: bold;
  color: #d49a6a; /* 标题的颜色 */
  text-align: left; /* 标题左对齐 */
  padding-left: 300px;
  margin-bottom: 10px; /* 取消下边距 */
  padding-right: 50px;
}

.description {
  font-size: 44px;
  color: white; /* 描述的颜色 */
  text-align: left; /* 描述左对齐 */
  padding-left: 300px;
  padding-right: 350px;
  margin-top: 15px; /* 取消上边距，如果需要的话 */
}

.images {
  padding-top: 100px;
  display: flex;
  align-items: flex-start; /* 改变对齐方式 */
}

.image-container {
  margin: 10px;
  text-align: left;
}

.image-container:nth-child(odd) {
  padding-top: 20px; /* 奇数容器（左边）增加上边距 */
  padding-right: 50px;
  padding-left: 10px;
  width: 55%;
}

.image-container:nth-child(even) {
  padding-top: 100px; /* 偶数容器（右边）不增加上边距 */
  width: 30%; /* 固定每个容器的宽度 */
  transform: scale(0.8);
}

.image-container img {
  max-width: 100%;
  height: auto;
}

.image-caption {
  font-size: 14px;
  margin-top: 5px;
  position: relative;
  display: inline-block;
  color: #d5aa80; /* 文字颜色 */
  text-transform: uppercase; /* 大写字母 */
  letter-spacing: 2px; /* 字母间距 */
  text-align: left; /* 向左靠齐 */
}

.image-caption::after {
  content: "";
  display: block;
  width: 100%;
  height: 2px;
  background-color: #d5aa80; /* 下划线颜色 */
  position: absolute;
  bottom: -5px; /* 距离文字底部的距离 */
  left: 0;
}
</style>
