<!--
 * @Date: 2025-02-14 12:21:17
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-14 13:19:07
-->

<!--  MyContact.vue  -->
<template>
  <div class="footer">
    <div class="contact-info">
      <p>sh1212121245@126.com</p>
      <p>17321176210</p>
    </div>
    <div class="logo">
      <img src="../../assets/logo1.png" alt="Logo" />
    </div>
    <div class="social-icons">
      <InstagramOutlined />
      <FacebookOutlined />
      <TwitterOutlined />
      <LinkedinOutlined />
    </div>
  </div>
</template>

<script>
import {
  InstagramOutlined,
  FacebookOutlined,
  TwitterOutlined,
  LinkedinOutlined,
} from "@ant-design/icons-vue";

export default {
  components: {
    InstagramOutlined,
    FacebookOutlined,
    TwitterOutlined,
    LinkedinOutlined,
  },
};
</script>

<style scoped>
.footer {
  background-color: black;
  color: #f7bc4e;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px;
  padding-bottom: 10px;
  border-top: 1px solid rgba(255, 255, 255, 0.2); /* 上边框 */
  position: relative; /* 添加相对定位以使用伪元素 */
  font-family: "Georgia", serif;
}

.footer::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px; /* 划线的高度 */
  background-color: rgba(255, 255, 255, 0.2); /* 划线的颜色 */
}

.contact-info,
.logo,
.social-icons {
  text-align: center;
}

.contact-info p {
  text-decoration: underline;
}

.social-icons > * {
  margin: 0 10px;
}

.logo {
  position: relative; /* 设置相对定位，以便伪元素定位 */
}

.logo::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 10%;
  width: 0;
  height: 4px; /* 划线的高度 */
  background-color: #ffffff; /* 划线的颜色 */
  transform: translateY(-50%);
  transition: width 0.8s ease; /* 添加过渡效果 */
}

.logo:hover::before {
  width: 80%; /* 鼠标悬停时划线宽度变为80% */
}

.logo img {
  max-width: 200px; /* 设置你希望的最大宽度 */
  max-height: 200px; /* 设置你希望的最大高度 */
  height: auto; /* 确保高度根据宽度自适应 */
  width: auto; /* 确保宽度根据高度自适应 */
}
</style>
