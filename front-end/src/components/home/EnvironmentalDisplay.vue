<!--
 * @Date: 2025-02-14 12:05:15
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-17 13:29:08
-->

<!--  EnvironmentalDisplay.vue  -->
  
<template>
  <div class="instagram-feed">
    <h3 class="feed-title">Other Ancient Wall</h3>
    <h1 class="main-title">Waiting for us to depart</h1>
    <div class="image-gallery">
      <div class="image-wrapper" v-for="(image, index) in images" :key="index">
        <img :src="image" alt="Instagram Image" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        require("../../assets/1.jpg"),
        require("../../assets/2.jpg"),
        require("../../assets/3.jpg"),
        require("../../assets/4.jpg"),
        require("../../assets/5.jpg")
      ],
    };
  },
};
</script>

<style scoped>
.instagram-feed {
  background-color: #8A8A8A;
  color: white;
  text-align: center;
  padding: 100px 0;
  font-family: 'Georgia', serif;
}

.feed-title {
  font-size: 0.8em;
  color: #d49a6a;
  letter-spacing: 2px;
  margin-bottom: 20px;
}

.main-title {
  font-size: 54px;
  margin-bottom: 120px;
  margin-top: 0px;
  letter-spacing: 1px;
}

.image-gallery {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.image-wrapper {
  margin: 0 10px;
  width: 250px;
  height: 500px;
  overflow: hidden;
}

.image-wrapper img {
  width: 100%;
  height: auto;
}
</style>
