<script>
    import Device from "./Device.svelte";

    export let data_url;

    let servers;
    let clients;

    let tableHeaders = ["设备名称", "ZeroTier网IP", "公网IP", "上次在线时间"];

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
    <table class="items-center bg-transparent w-full border-collapse ">
        <thead>
            <tr>
                {#each tableHeaders as th, i}
                    <th
                        class={i == 3
                            ? "hidden md:block md:px-6 px-2"
                            : "md:px-6 px-2"}>{th}</th
                    >
                {/each}
            </tr>
        </thead>

        <tbody>
            {#each servers as device}
                <Device {device} />
            {/each}
            {#each clients as device}
                <Device {device} />
            {/each}
        </tbody>
    </table>
{/if}

<style>
    th {
        @apply bg-gray-50 text-gray-500 align-middle border border-solid border-gray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left;
    }
</style>
