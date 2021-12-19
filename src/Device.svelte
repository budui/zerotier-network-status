<script>
    import Modal from "./Modal.svelte";

    let showModal = false;

    export let device;

    let records = {
        type: device.type,
        nodeId: device.nodeId,
        hidden: device.hidden,
        description: device.description,
        authorized: device.config.authorized,
        creationTime: new Date(device.config.creationTime).toLocaleString(),
        clientVersion: device.clientVersion,
    };

    function timeDifference(current, previous) {
        var msPerMinute = 60 * 1000;
        var msPerHour = msPerMinute * 60;
        var msPerDay = msPerHour * 24;
        var msPerMonth = msPerDay * 30;
        var msPerYear = msPerDay * 365;

        var elapsed = current - previous;

        if (elapsed < msPerMinute) {
            return "now";
        } else if (elapsed < msPerHour) {
            return Math.round(elapsed / msPerMinute) + " minutes ago";
        } else if (elapsed < msPerDay) {
            return Math.round(elapsed / msPerHour) + " hours ago";
        } else if (elapsed < msPerMonth) {
            return Math.round(elapsed / msPerDay) + " days ago";
        } else if (elapsed < msPerYear) {
            return Math.round(elapsed / msPerMonth) + " months ago";
        } else {
            return Math.round(elapsed / msPerYear) + " years ago";
        }
    }

    function handleClick() {
        console.log(device);
        showModal = true;
    }
</script>

{#if showModal}
    <Modal on:close={() => (showModal = false)}>
        <h2 slot="header" class="py-2 text-center">
            <span class="px-4 py-2">{device.name}</span>
        </h2>

        <ul>
            {#each Object.entries(records) as r}
                <li>{r[0]}: {r[1]}</li>
            {/each}
        </ul>
    </Modal>
{/if}

<tr
    class={device.online ? "bg-inherit" : "bg-yellow-100"}
    on:click={handleClick}
>
    <td class="md:px-6 px-2">{device.name}</td>
    <td class="md:px-6 px-2">
        {#each device.config.ipAssignments as ipAssignment}
            <code>
                {ipAssignment}
            </code>
        {/each}
    </td>
    <td class="hidden md:block md:px-6 px-2">
        {device.physicalAddress ? device.physicalAddress : "Unknown IP"}
    </td>
    <td class="md:px-6 px-2">
        {timeDifference(Date.now(), device.lastOnline)}
    </td>
</tr>

<style>
    td {
        @apply border-t-0 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4;
    }
</style>
