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
          <p>Games Library 🕹️</p>
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
        </div>
      </div>
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
