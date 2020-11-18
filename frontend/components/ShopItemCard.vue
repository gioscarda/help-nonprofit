<template>
  <div class="shop-item-card">

    <v-img v-if="!product.video" class="shop-item-image" :src="product.thumbnail"
           :key="product.order" transition="fade" contain/>

    <img class="shop-item-image" v-if="product.video" :src="product.video"/>

    <div class="shop-item-texts button-shadow-secondary-right">
      <span class="text-subtitle d-block">{{ texts.title }}</span>
      <h1 class="title-number">{{product.price}}€</h1>
      <h2 class="text-content d-block" v-html="product.title"/>
    </div>

    <div v-show="product.category.internal" class="mt-3">
      <v-row no-gutters>
        <v-col cols="6" class="help-font actions-info-col">
          <span class="available-quantity">{{available_quantity}}</span>
          <span class="available-info">{{ texts.subtitle }}</span>
        </v-col>
        <v-col cols="6" class="text-right actions-info-col">
          <v-btn class="button-shadow-error-left circle-button mr-2"
             fab text width="37" height="37" @click="removeFromShoppingCart(product)">
            <v-icon>{{minus_icon}}</v-icon>
          </v-btn>
          <v-btn class="button-shadow-primary-left circle-button"
             fab text width="37" height="37" @click="addToShoppingCart(product)">
            <v-icon>{{plus_icon}}</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </div>

    <div v-show="!product.category.internal" class="mt-3 text-right help-font">
      <span class="mr-2 available-info">{{ texts.content }}</span>
      <v-btn class="button-shadow-secondary-left circle-button"
             target="_blank" fab text width="37" height="37" :href="product.shop_link" >
        <v-icon>{{arrow_right_icon}}</v-icon>
      </v-btn>
    </div>

  </div>
</template>

<script>
  import { mdiArrowRight, mdiPlus, mdiMinus } from "@mdi/js";
  import VideoPlayer from "@/components/VideoPlayer";
  export default {
    name: "ShopItemCard",
    props: {
      product: Object,
      texts: Object
    },
    components: {
      VideoPlayer
    },
    data: () => ({
      products_in_the_cart: 0,
      arrow_right_icon: mdiArrowRight,
      plus_icon: mdiPlus,
      minus_icon: mdiMinus,
    }),
    computed: {
      available_quantity() {
        return this.product.availability - this.products_in_the_cart
      }
    },
    methods: {
      addToShoppingCart(product) {
        if (this.available_quantity > 0) {
          this.products_in_the_cart += 1
          this.$store.dispatch('addProductToShoppingCart', {
            product: product
          })
        }
      },
      removeFromShoppingCart(product) {
        if (this.available_quantity < this.product.availability) {
          this.products_in_the_cart -= 1
          this.$store.dispatch('removeProductToShoppingCart', {
            product: product
          })
        }
      }
    }
  }
</script>

<style lang="scss">
  .shop-item-card {
    .shop-item-texts {
      border: 2px black solid !important;
      text-align: center;
      background-color: white;
      /*margin-top: -5px;*/
      padding: 20px;
      z-index: 0;
      min-height: 100px;
      color: $accent-color;
    }
    .shop-item-image {
      z-index: 1;
      max-height: 70vh;
      max-width: 100%;
    }
    .text-subtitle {
      line-height: 100%;
      font-size: $font-size-20;
      font-family: "Crossten Light";
    }
    .title-number {
      position: relative;
      line-height: 100%;
      color: $secondary-color;
    }
    .text-content {
      line-height: 120%;
      font-family: "Crossten Bold";
    }
    .circle-button {
      border: 2px solid black !important;
    }
    .help-font {
      font-family: "Crossten Light";
      letter-spacing: 0.15rem !important;
    }
    .available-quantity {
      font-family: "Crossten Book";
    }
    .available-info {
      font-size: $font-size-12;
    }
  }
  @media #{map-get($display-breakpoints, 'md-and-down')} {
    .shop-item-card {
      /*.number-title {
        font-size: $font-size-50;
      }
      .text-content {
        line-height: 110%;
      }
      .shop-item-image {
        max-height: 50vh;
      }*/
      @media (max-width: 700px) and  (min-width:600px) {
        .actions-info-col {
          max-width: unset !important;
          display: inline-table !important;
        }
      }
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    /*.shop-item-card {
      padding-bottom: 5vh;
      .shop-item-texts {
        position: relative;
        text-align: center;
        min-height: unset;
        margin-left: 15%;
        margin-right: 15%;
      }
      .shop-item-image {
        margin-top: 0px;
        margin-bottom: 1vh;
      }
      .text-subtitle {
        margin-bottom: 1vh;
      }
      .text-content {
        line-height: 110%;
      }
    }*/
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    .shop-item-card {
      .shop-item-texts {
        margin-left: 0;
        margin-right: 0;
      }
    }
    .title-number {
      font-size: $font-size-40 !important;
    }
  }
</style>