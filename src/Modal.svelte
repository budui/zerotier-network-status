<script>
    import { createEventDispatcher, onDestroy } from "svelte";

    const dispatch = createEventDispatcher();
    const close = () => dispatch("close");

    let modal;

    const handle_keydown = (e) => {
        if (e.key === "Escape") {
            close();
            return;
        }
    };

    const previously_focused =
        typeof document !== "undefined" && document.activeElement;

    if (previously_focused) {
        onDestroy(() => {
            previously_focused.focus();
        });
    }
</script>

<svelte:window on:keydown={handle_keydown} />

<div class="modal-background" on:click={close} />

<div class="modal" role="dialog" aria-modal="true" bind:this={modal}>
    <slot name="header" />
    <hr />
    <slot />
    <hr />

    <!-- svelte-ignore a11y-autofocus -->

    <button autofocus on:click={close} class="px-4 py-2 my-2"> 关闭 </button>
</div>

<style>
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.3);
    }

    .modal {
        position: absolute;
        left: 50%;
        top: 50%;
        width: calc(100vw - 4em);
        max-width: 32em;
        max-height: calc(100vh - 4em);
        overflow: auto;
        transform: translate(-50%, -50%);
        padding: 1em;
        border-radius: 0.2em;
        background: white;
    }

    button {
        display: block;
    }
</style>
