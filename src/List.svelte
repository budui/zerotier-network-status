<script>
    import Device from "./Device.svelte";

    export let data_url;
    export let name;

    let servers;
    let clients;

    $: fetch(data_url)
        .then((r) => r.json())
        .then((data) => {
            refresh_devices(data);
        });

    function refresh_devices(devices) {
        servers = devices
            .filter((d, _) => {
                return d.name.match(/\d+_\w+_\d+/g);
            })
            .sort((a, b) => {
                return (
                    parseInt(a.name.match(/\d+/)[0]) -
                    parseInt(b.name.match(/\d+/)[0])
                );
            });

        clients = devices
            .filter((d, _) => {
                return !d.name.match(/\d+_\w+_\d+/g);
            })
            .sort((a, b) => {
                return a.lastOnline - b.lastOnline;
            });
    }
</script>

{#if servers}
    <div class="bg-indigo-700 mt-8 px-4 py-5 border-b rounded-t sm:px-6">
        <h3 class="text-2xl leading-6 font-2xl text-white">
            {name}
        </h3>
    </div>

    <div class="bg-white shadow overflow-hidden sm:rounded-md">
        <ul class="divide-y divide-gray-200">
            {#each servers as device}
                <Device {device} />
            {/each}
            {#each clients as device}
                <Device {device} />
            {/each}
        </ul>
    </div>
{:else}
    <div class="bg-indigo-700 shadow overflow-hidden sm:rounded-md p-4 my-10">
        <p class="text-xl  text-white">
            {name} Loading...
        </p>
    </div>
{/if}
