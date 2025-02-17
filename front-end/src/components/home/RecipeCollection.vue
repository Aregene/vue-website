<template>
  <div class="squarespace-container">
    <h1>古砖印象</h1>
    <div class="card-container">
      <div class="card" v-for="(item, index) in cards" :key="index">
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
        <div class="button-container">
          <a class="button" href="#">{{ item.linkText }}</a>
        </div>
      </div>
    </div>
  </div>
</template>







<script>
export default {
  data() {
    return {
      cards: [
        {
          title: '万佛阁(Wanfo Pavilion)',
          description: 'Wanfo Pavilion, a serene Buddhist temple, boasts over 10,000 Buddha statues, making it a popular pilgrimage site for devotees seeking solace.',
          linkText: 'LEARN MORE',
        },
        {
          title: '砖雕艺术馆(Brick Carving Art Museum)',
          description: 'Brick Carving Art Museum showcases an impressive array of brick carvings, highlighting the intricate artistry and cultural significance of this traditional craft from various historical periods.',
          linkText: 'LEARN MORE',
        },
        {
          title: '古砖窑遗址(The Ancient Brick Kiln Ruins)',
          description: 'The Ancient Brick Kiln Ruins is notable for its preserved brick kilns, providing a glimpse into the production methods of historical bricks, and offering a deep understanding of ancient industrial heritage.',
          linkText: 'LEARN MORE',
        },
        {
          title: '砖塔博物馆(Brick Tower Museum)',
          description: 'Brick Tower Museum features an extraordinary display of brick towers, emphasizing the architectural innovation and historical evolution of brick tower construction through the ages.',
          linkText: 'LEARN MORE',
        },
        {
          title: '古砖路遗址(The Ancient Brick Road Ruins)',
          description: 'The Ancient Brick Road Ruins is celebrated for its fragments of ancient brick roads, illustrating the materials and techniques used in historical road construction, and offering a tangible connection to the past.',
          linkText: 'LEARN MORE',
        },
        {
          title: '砖室墓博物馆(Brick Chamber Tomb Museum)',
          description: 'Brick Chamber Tomb Museum is distinguished by its exhibition of brick-lined tombs, showcasing the burial customs, artistry, and historical context of ancient societies through its comprehensive collections and displays.',
          linkText: 'LEARN MORE',
        },
        {
          title: '古砖博物馆(Ancient Brick Museum)',
          description: 'Ancient Brick Museum is renowned for its extensive collection of historical bricks, intricate exhibits, and educational programs that delve into the history and craftsmanship of ancient brick-making.',
          linkText: 'LEARN MORE',
        },
      ],
    };
  },
};
</script>

<style scoped>
.squarespace-container {
  background-color: #000;
  color: #fff;
  text-align: center;
  padding: 10px 0;
  padding-bottom: 100px;
}

h1 {
  font-size: 4em;
  margin-bottom: 50px;
  font-weight: bold;
  padding-bottom: 30px;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.card {
  background-color: #111;
  padding: 20px;
  width: 300px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
}

.button-container {
  position: relative;
  margin-top: 10px;
}

.button {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #f7bc4e;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #f7bc4e;
  overflow: hidden;
  z-index: 1; /* 确保文字始终在色块之上 */
}

.button::after {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #f7bc4e;
  transition: bottom 0.3s;
  z-index: -1; /* 确保色块始终在文字之下 */
}

.button:hover::after {
  bottom: 0;
}

.button:hover {
  color: #111; /* hover时改变文字颜色 */
  z-index: 1;
}

.card h2 {
  font-size: 1.5em;
  margin-bottom: 15px;
}

.card p {
  font-size: 1em;
  line-height: 1.5;
  margin-bottom: 20px;
}
</style>
