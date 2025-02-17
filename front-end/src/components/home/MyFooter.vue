<!--
 * @Date: 2025-02-14 12:35:41
 * @LastEditors: Aregene
 * @LastEditTime: 2025-02-17 13:06:31
-->

<!-- MyFooter.vue  -->
 
<template>
  <footer class="footer">
    <div class="line-1">
      &copy; 2025数说砖情社会实践团队. All rights reserved. A Lively Girl &
      Founder of <a href="#">SQUAR</a>
    </div>
    <div>
      <a href="#">Terms of Service</a>
      <a href="#">Return Policy</a>
      <a href="#">Privacy Policy</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "MyFooter",
};
</script>

<style scoped>
.footer {
  color: #fff;
  background-color: #000;
  text-align: center;
  padding: 20px;
  padding-top: 50px;
  padding-bottom: 50px;
  font-family: 'Georgia', serif;
}
a {
  color: #f7bc4e;
  margin: 0 10px;
  text-decoration: underline;
  font-size: 12px;
}
.line-1 {
    padding-bottom: 20px;
}
</style>
