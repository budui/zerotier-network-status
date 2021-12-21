<script>
	import List from "./List.svelte";

	let name = "ZeroTier Network Status";

	let data = [
		{ name: "Network_S", url: `api/network/S` },
		{ name: "Network_G", url: `api/network/G` },
	];
</script>

<main class="py-1 bg-gray-100 w-full min-h-screen">
	<div class="w-full xl:w-8/12 mb-12 xl:mb-0 px-4 mx-auto mt-24">
		<div class="pb-8 my-8">
			<h1
				class="md:text-6xl text-4xl text-zinc-800 font-semibold text-center"
			>
				{name}
			</h1>
		</div>
		{#each data as n}
			<List data_url={n.url} name={n.name} />
		{/each}

		<footer class="relative pt-8 pb-6 mt-16">
			<div class="container mx-auto px-4">
				<div
					class="flex flex-wrap items-center md:justify-between justify-center"
				>
					<div class="w-full md:w-6/12 px-4 mx-auto text-center">
						<div class="text-sm text-gray-500 font-semibold py-1">
							Made with by Ray Wang
						</div>
					</div>
				</div>
			</div>
		</footer>
	</div>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>
