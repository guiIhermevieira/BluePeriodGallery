<template>
  <div class="basic">
    <b-card title="Submissions" sub-title="Recent submitted artworks">
      <tr v-for="(artworks, index) in artworks" :key="index">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-1"
            label="Title:"
            label-for="input-1"
            description="The title of your artwork to be displayed."
          >
            <b-form-input
              id="input-1"
              v-model="form.title"
              type="title"
              placeholder="Enter artwork title"
              required
              >{{ artworks.description }}</b-form-input
            >
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Artist Name:"
            label-for="input-2"
          >
            <b-form-input
              id="input-2"
              v-model="form.artist"
              placeholder="Enter artist name"
              required
              >{{ artworks.description }}</b-form-input
            >
          </b-form-group>

          <label for="example-datepicker">Choose a date</label>
          <b-form-input id="input-3" v-model="form.year" type="date" required>{{
            artworks.description
          }}</b-form-input>
          <b-form-group
            id="input-group-3"
            label="Upload your image"
            description="Choose a nice file for your image!"
          >
            <b-form-file
              v-model="file1"
              :state="Boolean(file1)"
              placeholder="Choose the image or drop it here..."
              drop-placeholder="Drop image here..."
            ></b-form-file>
          </b-form-group>
          <b-form-group
            id="input-group-2"
            label="Description of Artwork:"
            label-for="input-2"
            description="Important for those who cannot see!"
          >
            <b-form-textarea
              id="textarea"
              v-model="text"
              placeholder="Enter something..."
              rows="3"
              max-rows="6"
              >{{ artworks.description }}</b-form-textarea
            >
          </b-form-group>
          <b-form-group
            id="input-group-1"
            label="Sold to:"
            label-for="input-1"
            description="If your art is already sold please inform to whom."
          >
            <b-form-input
              id="input-1"
              v-model="form.sold_to"
              type="title"
              placeholder="Enter owner of artwork"
              >{{ artworks.description }}</b-form-input
            >
          </b-form-group>
          <div class="side-by-side">
            <b-row>
              <b-col sm="6">
                <b-form-group
                  id="input-group-3"
                  label="Status:"
                  label-for="input-3"
                >
                  <b-form-select
                    id="input-3"
                    v-model="form.status"
                    :options="status"
                    required
                    >{{ artworks.description }}</b-form-select
                  >
                </b-form-group>
              </b-col>
              <b-col sm="6">
                <b-form-group
                  id="input-group-3"
                  label="Materials Used:"
                  label-for="input-3"
                >
                  <b-form-select
                    id="input-3"
                    v-model="form.materials_used"
                    :options="materials_used"
                    required
                    >{{ artworks.description }}</b-form-select
                  >
                </b-form-group>
              </b-col>
            </b-row>
          </div>

          <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group
              v-model="form.checked"
              id="checkboxes-4"
              :aria-describedby="ariaDescribedby"
            >
              <b-form-checkbox value="me"
                >I am aware that my arwork needs approval of gallery owners to
                be displayed.</b-form-checkbox
              >
            </b-form-checkbox-group>
          </b-form-group>
          <div class="buttons">
            <b-row>
              <b-col>
                <b-button type="submit" variant="primary">Submit</b-button>
              </b-col>
              <b-col>
                <b-button type="reset" variant="danger">Reset</b-button>
              </b-col>
            </b-row>
          </div>
        </b-form>
      </tr></b-card
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ArtGallery",
  data() {
    return {
      artworks: [],
      form: [
        {
          title: this.artworks.title,
          name: this.artworks.name,
          materials_used: this.artworks.materials_used,
          year: this.artworks.year,
          status: this.artworks.status,
          sold_to: this.artworks.sold_to,
          checked: this.artworks.checked,
          text: this.artworks.text,
          file1: this.artworks.file1,
        },
      ],
      show: true,
    };
  },
  methods: {
    getArts() {
      const path = "http://localhost:5000/submissions";
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
.center-details {
  align: center;
  padding: 60px;
}
</style>
