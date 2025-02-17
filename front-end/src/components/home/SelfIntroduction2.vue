<!--
 * @Date: 2025-02-13 23:07:44
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-17 13:27:31
-->
 <!--  SelfIntroduction2.vue  -->
<template>
  <div class="intro-container">
    <div class="text-section">
      <h1>古砖历史(History of Ancient Bricks)</h1>
      <p class="first-line">
        The history of ancient bricks can be traced back several thousand years, with evidence of their use in ancient civilizations such as Egypt, Mesopotamia, and China. 
      </p>
      <p>
        Initially, bricks were crafted from mud or clay and sun-dried or fired in kilns to enhance their durability. These early bricks were primarily used for construction purposes, including the building of temples, palaces, and defensive structures. 
      </p>
      <p>
        Their simplicity and versatility made them a staple material in ancient architectural practices.
      </p>
      <button @click="showMore">LEARN MORE →</button>
    </div>
    <div class="image-section">
      <img
        class="fade-in"
        src="../../assets/sotrefirst2.jpg"
        alt="个人简介图片"
      />
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      const img = this.$el.querySelector(".fade-in");
      if (img) {
        img.style.transform = "translateX(0)";
        img.style.opacity = "1";
      }
    }, 500);
  },
  methods: {
    showMore() {
      alert("更多信息...");
    },
  },
};
</script>

<style scoped>
.intro-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 120vh;
  background: #8A8A8A;
  color: #fff;
}

.image-section {
  flex: 1;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-section img {
  max-width: 90%;
  max-height: 100%;
  object-fit: cover;
  transform: translateX(100%);
  opacity: 0;
  transition: transform 3s ease-in-out, opacity 3s ease-in-out;
}

.text-section {
  flex: 1;
  padding: 20px;
  text-align: left;
}

.text-section h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.text-section p {
  font-size: 1.2em;
  margin-bottom: 20px;
}

.text-section button {
  padding: 30px 100px;
  font-size: 12px;
  border: 1px solid #f7bc4e;
  letter-spacing: 1px;
  background: transparent;
  color: #fff;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  z-index: 1;
  margin-left: 50px;
}

.text-section button::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0;
  background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23f7bc4e" fill-opacity="1" d="M0,160L48,176C96,192,192,224,288,229.3C384,235,480,213,576,192C672,171,768,149,864,144C960,139,1056,149,1152,165.3C1248,181,1344,203,1392,213.3L1440,224L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
  background-size: cover;
  z-index: -1;
  transition: height 0.5s ease-in-out;
}

.text-section button:hover::before {
  height: 100%;
}

.text-section button:hover {
  color: #fff;
}

.first-line {
  padding-top: 20px;
}
h1 {
  font-family: Georgia, serif;
  padding-left: 50px;
}

p {
  font-family: "Microsoft YaHei", sans-serif;
  font-size: 1.2em;
  letter-spacing: 0.5px;
  padding-left: 50px;
}
</style>
