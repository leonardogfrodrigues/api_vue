<!--<template>
  <div class="popup">
      <div class="popup-inter">
          <slot/>
          <button class= "popup-close">
              Fechar
          </button>
      </div>
  </div>
</template>
-->
<template>
  <teleport to="body">
    <div v-show="show" class="modal" ref="modal">
      <div
        ref="popover"
        class="popover"
        :style="{ top: popoverTop + 'px', left: popoverLeft + 'px' }"
      >
        <slot ref="content"></slot>
      </div>
    </div>
  </teleport>
</template>
<script>
export default {};
</script>

<style lang="scss" scoped>
.popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0.2);

  display: flex;
  align-items: center;
  justify-content: center;
  .popup-inner {
    background: #fff;
    padding: 32px;
  }
}
</style>
