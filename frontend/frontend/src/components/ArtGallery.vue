<template>
  <div class="basic">
    <b-card title="Blue Period Art Gallery" sub-title="Our artworks">
      <div class="mt-4">
        <tr v-for="(artworks, index) in artworks" :key="index">
          <h4>{{ artworks.title }}</h4>
          <b-card
            img-src="${artworks.image}"
            img-alt="Card image"
            img-left
            class="mb-3"
          >
            <b-card-text>
              {{ artworks.description }}
            </b-card-text>
          </b-card>
          <h4>{{ artworks.title }}</h4>
          <b-card img-src="${artworks.image}" img-alt="Card image" img-right>
            <b-card-text>
              {{ artworks.description }}
            </b-card-text>
          </b-card>
        </tr>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ArtGallery",
  data() {
    return {
      artworks: [],
    };
  },
  methods: {
    getArts() {
      const path = "http://localhost:5000/arts";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.artworks = res.data.artworks;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getArts();
  },
};
</script>

<style>
.mt-4 {
  margin-top: 4rem;
}
.basic {
  align: center;
  padding: 60px;
}
</style>
