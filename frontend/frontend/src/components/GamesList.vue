<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library 🕹️
          </h1>
          <hr />
          <br />
          <!-- alert message -->
          <button type="button" class="btn btn-success btn-sm">Add game</button>
          <br />
          <br />
          <table class="table table-hover">
            <!-- table head -->
            <thead>
              <tr>
                <!-- table header cells  -->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-goup" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy; All Rights Reserved 2023.
          </footer>
        </div>
      </div>
      <!-- first modal -->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGameForm.title"
              required
              placeholder="Enter game name"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-group"
            label="Genre"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              v-model="addGameForm.genre"
              required
              placeholder="Enter ganre"
            >
            </b-form-input>
          </b-form-group>
          <!-- checkbox -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group
              v-model="addGameForm.played"
              id="form-checks"
            >
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <!-- buttons -->
          <button type="submit" variant="primary">Submit</button>
          <button type="reset" variant="primary">Reset</button>

          <button></button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      games: [],
    };
  },
  methods: {
    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          this.games = res.data.games;
          console.log(res);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getGames();
  },
};
</script>
