<!--
 * @Date: 2025-02-13 23:00:28
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-17 10:03:34
-->

<!--  Header.vue  -->

<template>
  <div class="nav-header">
    <div class="logo-container">
      <div class="logo" />
    </div>
    <div class="hamburger-container" @click="toggleMenu">
      <div class="hamburger">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
    <transition name="slide">
      <div class="menu" v-if="menuOpen">
        <a @click="toggleMenu">Home</a>
        <a @click="toggleMenu">Information</a>
        <a @click="toggleMenu">Perception</a>
        <a @click="toggleMenu">About US</a>
      </div>
    </transition>
    <div class="content">
      <h1>
        Welcome to the website of the Social Practice Team for 'Numbers' and'
        Bricks'
      </h1>
      <div class="buttons">
        <button class="left-button">Hundred Brick Knowledge Base</button>
        <button class="right-button">Practical Style</button>
      </div>
    </div>
    <transition name="fade">
      <a-button
        v-if="showArrow"
        class="scroll-arrow"
        shape="circle"
        @click="scrollToNextSection"
      >
        <template #icon>
          <DoubleRightOutlined />
        </template>
      </a-button>
    </transition>
  </div>
</template>

<script>
import { DoubleRightOutlined } from "@ant-design/icons-vue";
import { Button } from "ant-design-vue";

export default {
  name: "NavHeader",
  components: {
    DoubleRightOutlined,
    AButton: Button,
  },
  data() {
    return {
      menuOpen: false,
      showArrow: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    scrollToNextSection() {
      window.scrollBy({
        top: window.innerHeight,
        behavior: "smooth",
      });
    },
    showScrollArrow() {
      setTimeout(() => {
        this.showArrow = true;
      }, 5000);
    },
  },
  mounted() {
    this.showScrollArrow();
  },
};
</script>

<style scoped>
.nav-header {
  background: url("../../assets/firstbackground.jpg") no-repeat center center;
  background-size: cover;
  height: 100vh;
  position: relative;
}
/*https://iphoto.mac89.com/photo/JPG-180514/180514_178/9PhJ3jaT8g_small.jpg*/
/* 添加伪元素作为模糊层 */
.nav-header::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8); /* 灰蓝色背景，高透明度 */
  backdrop-filter: blur(5px); /* 模糊效果 */
  z-index: 1; /* 确保模糊层覆盖在图片层之上，但内容层之下 */
}

.logo-container {
  position: absolute;
  top: 20px;
  left: 16px;
}

.logo {
  width: 220px;
  height: 210px;
  background: url("../../assets/logo1.png") no-repeat center/contain;
  transition: transform 0.5s ease-in-out;
  z-index: 998; /* 确保logo在最上层 */
  position: relative; /* 添加position属性以使z-index生效 */
}

.logo:hover {
  transform: translateY(-15px); /* 浮动效果 */
}

.hamburger-container {
  position: absolute;
  top: 20px;
  right: 16px;
  cursor: pointer;
  z-index: 1000;
}

.hamburger {
  width: 35px;
}

.bar {
  width: 35px;
  height: 5px;
  background-color: #fff;
  margin: 6px 0;
  transition: 1s;
}

.menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  color: white;
  z-index: 999;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直居中 */
  align-items: center;
}

.menu a {
  margin: 20px 0; /* 调整间距 */
  color: #fff;
  text-decoration: none;
  font-size: 28px; /* 更大字体 */
  font-family: "Georgia", serif; /* 可以选择其他字体 */
  text-shadow: 2px 2px 4px #000; /* 文本阴影增加艺术感 */
  transition: color 0.3s;
}

.menu a:hover {
  background: linear-gradient(to right, #efeaea, #746f5b); /* 黑金渐变色 */
  color: #fff; /* 文字颜色设置为白色 */
  background-clip: text; /* 使渐变色应用于文字 */
  -webkit-background-clip: text; /* 兼容性处理 */
  -webkit-text-fill-color: transparent; /* 兼容性处理 */
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 50px);
  text-align: center;
  color: white;
  position: relative;
  z-index: 2; /* 确保内容层在模糊层之上 */
}

h1 {
  font-size: 72px;
  margin-bottom: 20px;
  font-family: "Times New Roman", serif; /* 使用Arial Black字体 */
  font-weight: bold; /* 加粗 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5),
    -2px -2px 4px rgba(255, 215, 0, 0.5); /* 添加黄色和黑色的阴影效果 */
  color: white; /* 确保字体颜色为白色 */
  text-transform: uppercase; /* 将文本转换为大写 */
  letter-spacing: 10px; /* 增加字母间距 */
  animation: glow 1.5s infinite alternate; /* 添加闪烁动画效果 */
}

@keyframes glow {
  from {
    text-shadow: 0 0 5px rgba(233, 225, 223, 0.5),
      0 0 10px rgba(22, 22, 21, 0.5), 0 0 15px rgba(21, 21, 20, 0.5);
  }
  to {
    text-shadow: 0 0 10px rgba(159, 152, 164, 0.7),
      0 0 20px rgba(35, 34, 32, 0.7), 0 0 30px rgba(28, 28, 26, 0.7);
  }
}

.buttons {
  display: flex;
  justify-content: space-around; /* 增加按钮之间的间距 */
  width: 600px; /* 可以设置一个固定宽度来确保间距看起来合适 */
}

.left-button,
.right-button {
  margin: 10px;
  padding: 10px 20px;
  border: 4px solid white;
  background: transparent;
  color: white;
  cursor: pointer;
  font-size: 20px;
  transition: background 0.3s, color 0.3s;
  border-radius: 20px; /* 添加圆角 */
  letter-spacing: 5px;
}

.left-button:hover,
.right-button:hover {
  background: white;
  color: black;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 1.6s ease; /* 时间延长 */
}

.slide-enter {
  transform: translateX(-100%);
}

.slide-enter-to {
  transform: translateX(0);
}

.slide-leave {
  transform: translateX(0);
}

.slide-leave-to {
  transform: translateX(-100%);
}

.scroll-arrow {
  position: absolute;
  bottom: 50px; /* 调整箭头距离底部的距离 */
  left: 50%;
  transform: translateX(-50%);
  color: #d3d3d3; /* 淡灰色 */
  font-size: 14px; /* 箭头大小 */
  transition: opacity 0.5s, transform 0.5s;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: rotate(90deg);
  border: none; /* 移除边框 */
  background-color: transparent; /* 移除背景色 */
  z-index: 1001; /* 确保logo在最上层 */
  position: relative; /* 添加position属性以使z-index生效 */
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s, transform 0.5s, background-color 0.5s, color 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
  transform: translateX(-50%) scale(0.5);
  background-color: rgba(211, 211, 211, 0); /* 初始淡背景 */
  color: rgba(211, 211, 211, 0); /* 初始淡文字 */
}

/* 添加微弱白色闪烁效果 */
.scroll-arrow:hover {
  animation: flash 1.5s infinite alternate;
}

@keyframes flash {
  from {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
  }
  to {
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
  }
}
</style>
