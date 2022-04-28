<template>
  <div class="form">
    <b-card title="Submit your art">
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
          ></b-form-input>
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
          ></b-form-input>
        </b-form-group>

        <label for="example-datepicker">Choose a date</label>
        <b-form-input
          id="input-3"
          v-model="form.year"
          type="date"
          required
        ></b-form-input>
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
          ></b-form-textarea>
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
          ></b-form-input>
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
                ></b-form-select>
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
                ></b-form-select>
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
              >I am aware that my arwork needs approval of gallery owners to be
              displayed.</b-form-checkbox
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
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        title: "",
        name: "",
        materials_used: null,
        year: null,
        description: "",
        image: null,
        soldTo: "",
        checked: [],
        status: [],
      },
      materials_used: [
        { text: "Select One", value: null },
        "Oil Painting",
        "Marble Sculpture",
        "Wood Sculpture",
        "Metal Sculpture",
        "Glass Sculpture",
        "Paper Sculpture",
        "Stone Sculpture",
        "Wood",
        "Metal",
        "Glass",
        "Maquette",
        "Performance",
      ],
      status: [
        { text: "Select One", value: null },
        "Sold",
        "On Sale",
        "Display Only",
        "Private",
        "Auction",
        "Public",
      ],
      show: true,
    };
  },
  methods: {
    addArtWork(payload) {
      const path = "http://localhost:5000/submit";
      axios
        .post(path, payload)
        .then(() => {
          this.getArtWork();
          this.message = "Artwork submitted successfully";
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getArtWork();
        });
    },
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        title: this.form.title,
        artist: this.form.artist,
        materials_used: this.form.materials_used,
        year: this.form.year,
        description: this.text,
        image: this.file1,
        sold_to: this.form.sold_to,
        checked: this.form.checked,
        status: this.form.status,
      };
      this.addArtWork(payload);
      this.initForm();
      alert(JSON.stringify(this.form));
    },
    onReset(event) {
      event.preventDefault();
      this.form.title = "";
      this.form.name = "";
      this.form.materials_used = null;
      this.form.checked = [];
      this.form.status = null;
      this.form.year = null;
      this.form.description = "";
      this.form.image = null;
      this.form.soldTo = "";
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>

<style>
.form {
  padding: 60px;
  justify-content: center;
  display: flex;
  flex-direction: row;
}
.side-by-side {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.buttons {
  display: inline-flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>
