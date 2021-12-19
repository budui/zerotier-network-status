<script>
	import List from "./List.svelte";

	let data = [
		{ name: "Network_S", url: `http://localhost:5000/list.json` },
		{ name: "Network_G", url: `http://localhost:5000/list1.json` },
	];
</script>

<main class="py-1 bg-gray-100 w-full">
	<div class="w-full xl:w-8/12 mb-12 xl:mb-0 px-4 mx-auto mt-24">
		{#each data as n}
			<div
				class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded "
			>
				<div class="rounded-t mb-0 px-4 py-3 border-0">
					<div class="flex flex-wrap items-center">
						<div
							class="relative w-full px-4 max-w-full flex-grow flex-1"
						>
							<h3 class="font-semibold text-base text-gray-700">
								{n.name}
							</h3>
						</div>
						<div class="red-500"><p>黄色背景为掉线设备</p></div>
					</div>
				</div>
				<div class="block w-full overflow-x-auto">
					<List data_url={n.url} />
				</div>
			</div>
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
