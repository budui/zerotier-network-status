<script>
    import Modal from "./Modal.svelte";

    let showModal = false;

    export let device;

    let records = {
        type: device.type,
        nodeId: device.nodeId,
        zerotierIP: device.config.ipAssignments,
        physicalAddress: device.physicalAddress,
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

<li>
    <div class="block hover:bg-gray-50">
        <div class="px-4 py-4 sm:px-6">
            <div class="flex items-center justify-between">
                <p class="truncate">
                    {#each device.config.ipAssignments as ipAssignment}
                        <span on:click={handleClick}
                            class="px-2 py-2 font-semibold text-sm bg-neutral-400 text-white rounded-md shadow-sm opacity-100"
                        >
                            {ipAssignment}
                        </span>
                    {/each}
                    <span class="pr-4">{device.name}</span>
                </p>
                <div class="ml-2 flex-shrink-0 flex">
                    {#if device.online}
                        <p
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"
                        >
                            Online
                        </p>
                    {:else}
                        <p
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"
                        >
                            Offline
                        </p>
                    {/if}
                </div>
            </div>
            <div class="mt-2 flex justify-between flex-col md:flex-row ">
                <div class="flex text-gray-700">
                    <p class="flex flex-col md:flex-row text-ellipsis ">
                        <span class=""
                            >{device.physicalAddress
                                ? device.physicalAddress
                                : "Unknown IP"}</span
                        >
                        {#if device.description}
                            <span class="md:pl-4 text-black"
                                >{device.description}</span
                            >
                        {/if}
                    </p>
                </div>
                {#if !device.online}
                    <div class="ml-2 flex  justify-end">
                        <p class=" text-sm font-light ">
                            {timeDifference(Date.now(), device.lastOnline)}
                        </p>
                    </div>
                {/if}
            </div>
        </div>
    </div>
</li>
