<template>
  <section id="projects-details-section-1" class="padding-level-3">

    <div class="section-title-left">
      <h1 class="section-title">{{project.title}}</h1>
    </div>

    <v-row no-gutters>
      <v-col cols="12" md="6" class="section-text">
        <h2 class="text-subtitle d-block" v-html="project.subtitle"/>
        <div class="text-content" v-html="project.description"/>
      </v-col>
      <v-col cols="12" md="6" class="section-map">
        <div id="map-wrap">
          <client-only>
            <l-map :center="[project.longitude, project.latitude]" :zoom="15">
              <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
              <l-marker :lat-lng="[project.longitude, project.latitude]"></l-marker>
            </l-map>
          </client-only>
        </div>
        <div class="coordinates-address text-right">
          <span class="coordinates">{{parseFloat(project.latitude)}}</span>,
          <span class="coordinates">{{parseFloat(project.longitude)}}</span>
          <div class="address">
            <h3>{{project.country}}</h3> -
            <h3>{{project.region}}</h3> -
            <h3>{{project.city}}</h3>
            <br>
            <span>{{project.address}}</span>
          </div>
        </div>
      </v-col>
    </v-row>

  </section>
</template>

<script>
  export default {
    name: "Section_1",
    props: {
      data: Object,
      project: Object
    },
    /*head() {
      if (this.data) {
        return {
          meta: this.data.meta_tags
        }
      }
      return []
    }*/
  }
</script>

<style lang="scss">
  #projects-details-section-1 {
    .section-text {
      padding-right: 2vw;
      line-height: 100%;
    }
    .section-map {
      display: flex;
      flex-direction: column;
    }
    .text-subtitle {
      line-height: 120%;
      margin-bottom: 2vh;
    }
    #map-wrap {
      height: 100%;
      z-index: 0;
    }
    .coordinates-address {
      font-family: "Crossten Book";
      font-size: 20px;
      padding-top: 1vh;
    }
    .address {
      font-family: "Crossten Thin";
      font-size: 20px;
      padding-top: 1vh;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    #projects-details-section-1 {
      .project-subtitle {
        font-size: 25px;
      }
      .project-description {
        font-size: 20px;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #projects-details-section-1 {
      .section-text {
        padding-right: 0px;
      }
      .section-map {
        height: 70vh;
        margin-top: 4vh;
        margin-bottom: 4vh;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #projects-details-section-1 {
      .project-subtitle {
        font-size: 20px;
      }
      .project-description {
        font-size: 18px;
      }
      .coordinates-address {
        font-size: 18px;
      }
      .address {
        font-size: 18px;
      }
    }
  }
</style>
