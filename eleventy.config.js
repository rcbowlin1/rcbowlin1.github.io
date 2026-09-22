module.exports = function (eleventyConfig) {
  // Copy CSS straight through to the built site.
  eleventyConfig.addPassthroughCopy("src/css");

  // Human-readable dates for posts (e.g., "September 22, 2026").
  eleventyConfig.addFilter("readableDate", (value) => {
    return new Date(value).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
