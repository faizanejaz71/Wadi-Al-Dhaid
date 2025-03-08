
const swiper = new Swiper('.swiper.social-swiper', {
  // Optional parameters
  slidesPerView: 4,
  spaceBetween: 20,
  loop:true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-custom-button-next',
    prevEl: '.swiper-custom-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  breakpoints: {
      320: {
          slidesPerView: 2,
          spaceBetween: 10
      },
      640: {
          slidesPerView: 3,
          spaceBetween: 20
      },
      1048: {
          slidesPerView: 4,
          spaceBetween: 20
      }
  },
});

const swiper2 = new Swiper('.swiper.reviews-swiper', {
  // Optional parameters
  slidesPerView: 3,
  spaceBetween: 20,
  loop:true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-custom-button-next',
    prevEl: '.swiper-custom-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  breakpoints: {
      320: {
          slidesPerView: 1,
          spaceBetween: 10
      },
      640: {
          slidesPerView: 2,
          spaceBetween: 20
      },
      1048: {
          slidesPerView: 3,
          spaceBetween: 20
      }
  },
});
const swiper3 = new Swiper('.swiper.rent-swiper', {
  // Optional parameters
  slidesPerView: 3,
  spaceBetween: 20,
  loop:true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-custom-button-next',
    prevEl: '.swiper-custom-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  breakpoints: {
      320: {
          slidesPerView: 1,
          spaceBetween: 10
      },
      640: {
          slidesPerView: 2,
          spaceBetween: 20
      },
      1048: {
          slidesPerView: 3,
          spaceBetween: 20
      }
  },
});
