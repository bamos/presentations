# Agent notes

This file separates reusable writing preferences from instructions for one
paper. Current user instructions take precedence over these defaults.

**Agents working on another paper:** retain the general guidance, but remove
instructions inherited from an old paper from your copy. Replace the isolated
paper-specific section with the current paper's scope, notation, layout,
build, and validation instructions, after checking its sources. Do not change
the old paper's file or invent conventions for the new one. Keep project names,
paths, commands, counts, and formatting choices out of the general section.

---

# General: writing workflow for any paper

Rules that quote LaTeX commands (run-in headings, `\label` aliases, citation
locators) assume a LaTeX paper with natbib and cleveref. Skip those on other
templates and keep the rest.

## Default editorial pass

- Aim to deliver a draft close to the writer's preferred final state. Apply
  established preferences proactively across the document. Before presenting
  a revision, review the argument, flow, notation, attribution, examples, and
  rendered layout. Anticipate concerns raised in earlier feedback and resolve
  analogous problems without waiting for another comment. Preserve the
  writer's voice and the agreed scope.
- Batch meaningful editorial choices into a small set of proposals. Once the
  user selects a direction, carry out the complete pass and make routine
  decisions independently. Reserve further questions for choices that
  materially change meaning, emphasis, scope, or structure.

## Reviewing a diff

- Leave edits unstaged and uncommitted by default so the user can review the
  cumulative diff across writing passes. Stage, commit, or push only when
  explicitly instructed. A request to commit one version does not authorize
  automatic commits of later passes. Preserve pre-existing staged work.
- Preserve the writer's voice. Prefer the smallest useful edit over a generic
  rewrite. Keep deliberate informality and enthusiasm in social writing.
  Formatting work is not permission to rephrase unrelated prose.
- For meaningful choices about wording, emphasis, organization, or presentation,
  propose two or three concrete numbered alternatives by default. Recommend
  one briefly, show enough context to judge it, and wait for a selection.
  The user should not need to request alternatives each time. Apply clear
  corrections, exact replacements, and already-approved edits directly.
  Do not fold declined proposals into later edits.
- For every comment, identify the underlying concern and consider other
  relevant improvements throughout the document, beyond exact wording matches.
  Check related explanations, notation, examples, captions, and structure.
  Apply the agreed direction consistently without asking about each occurrence.
- For annotated PDFs, account for every comment, strikeout, arrow, and placement
  request. Group related edits, clarify ambiguous marks, and check that each
  annotation is addressed or explicitly left pending rather than silently missed.
- Lead with what you verified (build, tests, math), then the proposals in
  priority order, then judgment calls last. Say which items are judgment calls.
- Keep proposals separable. A rename and a merge, or a restoration and a
  rewording, go in separate items so each can be accepted alone.
- Give the proposed replacement text, not just the complaint.
- Inventory what the diff removed, not only what it changed. Flag dropped
  results, caveats, concrete examples, and limitations statements separately
  from wording changes; the author may not have meant to lose them.
- Check claims against the source. If the author believes a citation or
  sentence exists, grep the `.tex` files and git history before agreeing,
  and add a missing bib entry rather than a citation to nothing.
- Re-read a section file immediately before editing it. The author edits
  concurrently, and a stale read can overwrite their newer version.
- Restore from the original only what was explicitly requested; propose other
  restorations as separate numbered items.

## Prose

- Use “and” rather than ampersands in prose and figure labels, with an Oxford
  comma in lists of three or more items. Preserve official names and quotations.
- For technical papers, write for researchers and graduate-level readers with
  the relevant background, including readers outside the exact specialty.
  Assume standard mathematics and common tools in the field, but not familiarity
  with the paper's particular mechanisms, derivations, or implementation choices.
- Keep the prose friendly and easy to follow through clear motivation,
  transitions, concrete explanations, and brief reminders. Do not make it
  elementary or belabor routine facts. Explain a non-obvious step rather than
  labeling it obvious or leaving the reader to reconstruct the argument.
- Give the abstract and introduction different jobs. The abstract summarizes
  the problem, contribution, and result. The introduction develops the
  motivation and mechanism. Revisit ideas with more depth rather than repeating
  sentences or definitions.
- Give sentences a clear focus and connect them into a coherent paragraph.
  State the fact, then the consequence. Avoid semicolons in prose and filler such
  as "we note that" or "it is worth mentioning".
- Avoid slogan-like writing: paired imperatives, forced contrasts, vague
  aphorisms, and generic takeaway lines written for rhetorical symmetry.
  "Preserve the choices. Recompute the values" is an example to avoid.
  Name the actual objects and operations, such as "Use the recorded expert IDs
  during training," or omit the line if the figure already explains it.
  Apply this to titles, slide text, captions, outlines, and spoken prose.
  Sparse slides do not need a tagline to fill the space.
- Do not shorten prose by dropping necessary words, especially articles such
  as "a", "an", and "the". Keep subjects and connecting words needed for natural,
  grammatical sentences. Cut redundancy rather than making prose telegraphic.
- Do not add notes that state the obvious (e.g., that a vector identity holds
  componentwise). Remove redundancy without deleting useful motivation or
  inline reminders. Omit sentences that merely announce the document's layout
  or restate self-evident consequences.
- Do not say the same thing at the start and end of a paragraph.
- Before-and-after examples of these rules:
  - Filler. "It is worth noting that the gradient vanishes at equality."
    becomes "The gradient vanishes at equality."
  - Obvious note. "Vector products and scalar subtraction are evaluated
    componentwise." is dropped when the notation is standard.
  - Repeated frame. A paragraph that opens with "The final correction in
    \cref{eq:fix} leaves the gradient unchanged" and closes with "so the
    final correction in \cref{eq:fix} is harmless" keeps only the opening.
  - Hedging. "Adam amplifies this error during training." becomes "Adam can
    amplify this error." unless the experiment measured training.
  - Derivation. A reproduced optimizer first-step formula becomes a citation
    to the paper that derived it when only its conclusion is used.
  - Section opening. "This section is organized as follows." becomes one
    sentence on what the section fixes and why it comes next.
- Motivate definitions and equations before introducing them. Explain the
  basic computation, failure, and correction in prose and equations before
  referring to code. Readers should not need to inspect a listing to understand
  the argument. Mark transitions between different questions, such as values
  and derivatives.
- Put shared setup before the variants that use it. Reuse an existing issue
  when its mechanism is shared and explain what changes in the new setting.
  Introduce a separate issue only for a meaningful distinction. Keep boxes
  focused on their essential definitions, issues, or corrections, with
  motivation and extended discussion in the surrounding prose.
- Cite a published derivation instead of reproducing it when the paper only
  needs the conclusion.
- Hedge unverified claims with "can" or "may"; state verified ones plainly.
  Do not claim training or downstream outcomes the experiments do not measure.
- Introduce sections with enough context to explain their purpose and connection
  to the argument, without adding boilerplate descriptions of the structure.
- Prefer bold run-in paragraph headings (`\textbf{...}`) over new
  subsections for short topics. Phrase headings as the claim when possible
  ("Numerical issues are exacerbated at lower precision.").
- Repeated structures use a consistent template where they serve the same purpose.
- Make question titles unambiguous about the actor and the object of the
  action. Name them explicitly when "we", "it", or an omitted subject could
  obscure which model, quantity, or decision the question concerns.
- Keep applications focused on the paper's contribution. Give enough context
  and mathematics to show where the result matters, without turning an
  application into a field survey or deriving machinery the argument never uses.
- Use numerical detail selectively in prose. Explain the behavior and its
  significance. Include individual values when they establish scale or
  demonstrate a failure, rather than reciting outputs and error percentages
  already visible in figures.
- An exploratory question about a related topic is not a request to add it.
  Include it only if it helps the argument. Omit abandoned implementation history
  unless it explains a current choice or tradeoff.

## Notation, claims, and references

- Preserve technical meaning during polishing. Do not silently strengthen
  claims, drop assumptions, or blur exact and approximate results. Explain
  proposed changes to the claim separately from wording improvements.
- Use consistent notation and define symbols where first needed. Avoid aliases
  and intermediate names that add no meaning. State differentiation variables,
  fixed quantities, inputs, and assumptions when they affect interpretation.
- Separate mathematical identities, implementation behavior, experimental
  evidence, and conjectures. State limitations where relevant without repeating
  them throughout the document.
- Refer to equations, sections, and boxes by labels, never by hard-coded
  numbers. Confirm printed numbers against the current build before quoting
  them in discussion. Use citation commands rather than manually reconstructed
  author names and years.
- Do not use "above" or "below" to reference material. Every reference should
  identify its actual target: the named result, method, equation, section,
  figure, table, or listing. Use the most specific relevant target. For an
  unnumbered passage, name the concept or briefly restate the needed context,
  rather than using a label that resolves to an unrelated enclosing number.
- Give each referenced section, equation, or environment one canonical label
  that describes its current content. When renaming or moving it, update its
  references and remove obsolete aliases. Put section labels immediately after
  their headings, and do not label an unnumbered paragraph as though it were a
  separate section.
- Cite with locators where possible: `\citet[Section~3]{...}`,
  `\citep[Eq.~(9)]{...}`. Each borrowed identity names its source.
- Verify citations against the specific claims they support. Distinguish
  foundational results from recent applications and the paper's contributions.
  Name the researchers or method instead of ambiguous references such as
  "the authors."
- Integrate citations into the argument. Use narrative attribution when naming
  a contribution and parenthetical citations for supporting context. Place each
  citation beside the claim it supports, rather than attaching a list of papers
  to a paragraph containing several different claims. Group references only
  when they support the same point. Avoid repeating the same citation in
  adjacent sentences when the attribution remains clear. Do not credit a
  recent application paper with a standard result or add references merely to
  make the bibliography longer.

## Verification after a paper edit

- Compare the revision with the actual text immediately before the edit,
  including earlier uncommitted changes, rather than relying on an older Git
  commit. Account for authorized additions and deletions. Check both for
  omitted content and for new claims the original did not support.
- Check relationships as well as individual words and values. Conditions,
  exceptions, negation, comparisons, bounds, and certainty must still apply to
  the correct claim. Check numbers and units together, and verify mathematical
  operands, differentiation variables, and assumptions. Matching words or
  numbers alone does not establish that the meaning is unchanged.
- Repair unintended changes in meaning before presenting the revision, while
  retaining useful improvements to the prose. Make this a routine internal
  check, not a lengthy report to the user. Surface substantive unresolved
  differences or choices that need the author's judgment.
- After scope or structure changes, reconcile the abstract, introduction,
  overview, applications, conclusions, and examples with the body.
- When refreshing a document from a revised source, audit removals as well as
  additions. An older draft or a surviving figure asset does not establish
  that a withdrawn detail should remain. Reconcile affected prose, tables,
  figures, and authoring guidance; flag source contradictions or apparent
  errors instead of copying them mechanically.
- Run the paper's check target when it has one (see the paper-specific
  section). Otherwise build and check for overflow, undefined references,
  and duplicate labels. Inspect freshly rendered affected and neighboring
  pages, and reinspect after the final layout change.
- After removing an environment or equation, grep for its label to make sure
  nothing still references it.
- Keep any counts stated in the intro (numbered issues, propositions, listings)
  consistent with the body.

- Spelling and grammar checkers need prose extracted from the LaTeX first
  (math, citations, labels, and environments stripped), or they report mostly
  markup. Keep a project wordlist and a list of ignored rules so the check
  stays near zero false positives. A check that cries wolf gets skipped.
- Short last lines of paragraphs (one or two words) are worth a scan of the
  rendered PDF. Fix them with a small rephrase, never with spacing hacks.

## Generated files

- Follow the paper's policy for generated artifacts. Export scripts may leave
  orphaned outputs, so check for obsolete generated files after renaming or
  dropping a listing, then regenerate affected outputs.
- Never hand-edit an extracted listing. Change the source and re-export.

## Code paired with the paper

- Keep examples general, with meaningful parameters rather than hard-coded
  experimental inputs. Display the implementation actually evaluated, or
  clearly identify a simplification. Explain necessary conditions and shared
  helpers without filling listings with incidental plumbing.
- Terminology in prose, code identifiers, JSON keys, and captions must match.
  Renames must include compound identifiers and saved result keys.
- Run checks appropriate to code changes without rerunning numerical experiments
  for prose-only edits. Note pre-existing lint findings and do not add to them.

## Polishing and fresh-reader review

- Treat every request to polish as a thorough review of the whole current
  paper unless the user explicitly narrows the scope. Read the source and
  rendered document, covering as much as possible: argument and flow,
  mathematical claims and notation, citations and attribution, prose and
  grammar, examples and evidence, cross-references, captions, and page layout.
  Do not stop at the latest edits, a sample of pages, or automated checks.
  Report areas that could not be verified. Keep edits focused and preserve
  the writer's voice, proposing meaningful changes as usual.
- Audit labels and their targets, including unused aliases, misleading names,
  duplicate labels, and references left over from an earlier structure. Check
  the printed number and link destination after updating the references.
- Check source organization as well as the rendered paper. Use either one
  manuscript file or a consistent split into section files. In a split paper,
  keep the main file focused on document assembly, put substantive prose in
  section files, and keep shared formatting in one place. Avoid leaving some
  major sections embedded in the main file or scattering short paragraph
  fragments across files. Update build tools and documentation when files move,
  and verify that a structural cleanup preserves the content and layout.
- For a split LaTeX paper, prefer one file per top-level section, with filenames
  numbered to match the document. Keep subsections in their parent section's
  file, and keep the abstract and acknowledgments inline in the main file.
- Keep reusable style files independent of a particular paper. Derive PDF
  metadata from the document's title and author instead of hard-coding it.
  Keep paper metadata and project paths in the manuscript.
  Make venue-specific patches conditional on the selected
  template. Prefer a single shared style file over an extra preamble file,
  and verify reusable formatting with a standalone document.
- Keep formatting decisions in the template or shared preamble. Remove
  redundant paragraph commands such as repeated `\noindent` when indentation
  is already disabled, and avoid accumulating local spacing overrides for a
  document-wide preference. Keep necessary exceptions narrowly scoped and
  inspect the rendered result after cleanup.
- Run a reference audit during a full polish pass and after bibliography
  changes. Prefer [RefChecker](https://github.com/markrussinovich/refchecker)
  to flag nonexistent works and malformed or mismatched metadata. Check the
  references actually cited in the current manuscript. Treat unmatched entries,
  access failures, and checker suggestions as findings to investigate, not proof
  of hallucination. Verify them against the cited version's primary source.
- Pair the metadata check with a claim-by-claim citation audit. Read the
  relevant primary-source passages and check each citation's claim and exact
  locator. Distinguish an algebraic identity from a stable implementation,
  a result stated in the source from a derivation using it, and foundational
  work from a later application. Credit established ingredients where first
  introduced, rather than only in related work.
- Check source versions and errata, including whether a reported bug remains
  in the cited implementation. State whether verification used full text,
  an abstract, or metadata only. Do not present inaccessible material as read
  or a failed search as evidence that no prior work exists. Record unresolved
  claims and propose focused corrections without adding irrelevant background.
- Reference checking is an audit, not a bibliography rewrite. Do not apply
  generated corrections wholesale or silently replace preprints with published
  versions. Preserve citation keys, full author names, title capitalization,
  locators, formatting, and intentional version choices. Propose substantive
  changes for review, and make only verified, minimal corrections within the
  user's authorized scope. Report unresolved entries and checker limitations.
- Read the revised material as an intended reader who has not seen the
  conversation. Use only the manuscript and the audience's assumed background
  to check that the problem, contribution, assumptions, and evidence are clear.
  Check that motivation, terminology, and transitions stand on their own, and
  that readers can distinguish what the results establish from what remains
  uncertain.
- Treat visual polish as part of finishing the document. Read a fresh PDF page
  by page at its intended reading size, checking flow across page boundaries
  as well as individual elements. Successful compilation is not a visual check.
- Keep figures, listings, and tables near the text they support, preferably at
  the top of a page. Group related examples where useful and make it clear which
  caption belongs to which object. Avoid stacks of unrelated floats that
  interrupt the argument or appear to belong to the wrong section.
- Each experimental panel should demonstrate a relevant failure, correction,
  limitation, or purposeful comparison. Omit redundant tables and uninformative
  panels. Use suitable examples, clear labels, and comparable panel dimensions
  and legends. Keep figure captions focused on takeaways and listing titles short.
- Check heading hierarchy, wording, alignment, and spacing for consistency.
  Keep headings with the text they introduce. Balance space around equations,
  boxes, plots, and captions without making the page feel cramped.
- Look for dangling words, isolated references, awkward caption or table-cell
  wraps, and single lines stranded across page boundaries. Prefer small,
  voice-preserving rephrases, sensible nonbreaking groups, or subtle typesetting
  adjustments. Do not change meaning, shrink text excessively, or accumulate
  brittle spacing hacks just to save a line. Enlarge figures to check collisions
  and clipping, and inspect the final render after fixes.
- Prefer natural page flow. Avoid manual page breaks or forced float placement
  merely to make one page look better. Adjust grouping, float preferences, or
  modest spacing first, rather than pinning content to a particular page number.

---

## Presentation design

### Content and emphasis

- Prefer a figure, a concrete example, or a compact table to prose describing
  what the audience can already see. Keep connective narration, personal
  background, routine implementation details, and source qualifications in
  speaker notes unless they are needed to interpret the slide. A request to
  mention something does not automatically call for more visible text.
  Do not replace deleted narration with another slogan or summary sentence.
- Titles should identify the subject, mechanism, or question. Avoid generic
  labels such as “The shortcut,” unnecessary title-ending colons, and vague
  qualifiers such as “current practice.” Keep ordinary slide titles left aligned
  and prefer one line when it fits naturally, without shrinking individual titles.
- Match the opening and closing title typography, author row, and metadata.
  Add the closing recap within that same visual language. Rebalance the opening
  as a group when it has less content, rather than changing its type sizes.
  Keep the recap and navigation link aligned to the content margin.
- Main claims, conditions, definitions, and diagram labels use charcoal. Reserve
  gray for secondary details, parentheticals, source credits, and intentionally
  inactive items. Keep inline parentheticals at the surrounding text size. Do not
  gray a whole important sentence or an essential mathematical condition merely
  because it is explanatory. Inspect the hierarchy instead of recoloring every
  parenthesis blindly.
- Proactively add selective bold emphasis when slide prose looks visually flat.
  Prefer one or two short, content-bearing phrases that identify the mechanism,
  contrast, constraint, or measured result, usually one to four words. Examples:
  “semantically defined,” “concurrently,” and “preference for verbosity.” Use
  comparable emphasis for paired ideas. Keep the rest of the sentence regular,
  including necessary qualifications; do not bold filler or whole paragraphs.
  Preserve explicit exceptions for regular-weight diagram labels and check the
  rendered line breaks after adding emphasis.
- Omit terminal periods from standalone slide sentences, bullets, annotations,
  and captions. Preserve punctuation in quotations, abbreviations, source titles,
  equations, multi-sentence prose, and notes. Keep short definitions and inline
  qualifiers on one line when possible instead of stacking separate labels.

### Grouping, alignment, and spacing

- Keep the gap within a group smaller than the gap between groups: portrait and
  name, heading and description, figure and credit, equation and annotation.
  Use consistent internal padding, with visible clearance above box headings.
  Do not add blank lines to one member of a repeated layout when its peers are tight.
- Use a light horizontal rule to separate substantive content from a footer or
  navigation link. When an outline starts beneath a rule, a matching rule beneath
  it separates the whole outline from the footer. Align both rules with the
  content margins, match their color and weight, and leave clear space around them.
- Use indentation, aligned rows, and quiet rules to make text easy to scan.
  Add a pale box when it clarifies a real group, such as a paper introduction,
  prompt excerpt, plot, or concise qualification. Do not box every sentence.
  A heading inset into a border needs a clean background gap around the text.
- Give peer elements the same typography. Never shrink one repeated item solely
  because it has more words. Adjust the layout or wrap it while preserving the
  hierarchy. Align descriptions beneath headings rather than beneath list numbers.
- In side-by-side comparisons, align headings and image regions and leave a real
  gutter. Keep each image, caption, and reference within its column. Put a vertical
  divider in the gutter with clearance on both sides, not against an image edge.
- Balance the occupied areas of the slide. Remove excessive gaps between titles,
  figures, and captions before shrinking content. Enlarge the main figure when
  extra commentary is removed; do not fill the available room with more text.

### Diagrams and equations

- Choose flow direction to fit the actual computation. Prefer straight arrows
  for simple paths and rounded orthogonal branches for parallel paths. Avoid
  pointed forks and broad shallow curves immediately beneath an input label.
  A centered stem can branch horizontally into independent computations and
  merge through a matching route into one centered output arrow. Preserve
  established curved connectors when they explain a more complex flow clearly.
- Trace every connector. Its tail must visibly belong to its source, its head
  must enter the intended target, and its route must clear text and other shapes.
  Leave a visible shaft between a merge and its target; do not reduce it to an
  arrowhead. Do not add dots at joins. Use consistent stroke widths, arrowheads,
  and corner radii within a diagram. A connected callout's border, leader, and
  outline should use the same accent and stroke weight.
- Make sample counts and data dependencies visible. Distinguish operations from
  outputs: if a judge produces a preference, put the comparison inside the judge
  block when this avoids an unnecessary extra block. Show analogous operations
  with the same kinds of outputs. Connect training losses to the pairs that feed
  them. Keep a feedback loop recognizable as a loop with labeled quantities.
- Use the same notation in diagrams and equations. A sampled candidate is an
  individual point, not a distribution. Axis labels must name the quantity
  actually plotted, such as a score rather than a probability. Keep schematic
  interpretations and limitations in the notes.
- Pair important equations with a useful visual on the same slide when possible.
  Separate a plot from surrounding equations with a quiet outline or rule rather
  than crowding them together. Short gray term labels should point to the actual
  terms, with leaders clear of subscripts, brackets, and fraction bars. Overlay
  annotations without shifting the established layout when requested.
- Match geometry, positions, notation, colors, and type sizes across analogous
  methods. Share the diagram definition where practical so a spacing fix applies
  to both explanations. Copy an approved source diagram faithfully when asked,
  including its stages, branches, arrows, and visual organization.

### Tables, examples, and builds

- Show the overview chart from the start of a category/example sequence. Place
  the current example beside it so the audience need not reconstruct the mapping
  later. Keep chart geometry and colors fixed; prefer bolding the current legend
  entry to dimming, exploding, or outlining slices.
- Keep geometry fixed across physical builds and change only the relevant content
  or emphasis. An annotation reveal should leave the underlying figure in place.
  Use a separate build only when it adds a useful step, not to repeat a slide for
  a small “this talk” label or other narration.
- Size a supporting table to its role rather than letting it dominate the slide.
  Use aligned columns, consistent row padding, and a restrained highlight for
  the selected row. Prefer full-width rows for parallel prose topics rather than
  mixing full-width sections with unrelated half-width blocks.
- Let result charts and tables carry their visible comparisons. Omit captions
  that merely restate the numbers or the direction already shown on an axis.
  Retain useful qualifications or experimental distinctions, optionally
  in one quiet callout. Put units beside values when that avoids ambiguous labels.
- Set actual prompt excerpts in a readable monospaced font. Show the distinctive
  criterion or decision rule, not generic role-setting boilerplate. Preserve
  quoted wording and identify the source. Label constructed examples as examples,
  keeping detailed provenance in notes.

### Images, credits, and footers

- Use supplied logos and artwork without redrawing them, preserving proportions.
  Balance logos by visible size and weight rather than identical file dimensions;
  transparent or white margins can make equal-size images look unequal. Center
  them within their peer rows. Use matching portrait shape, diameter, border,
  framing, and name baselines, with a tight portrait-to-name gap.
- Keep illustrative imagery subordinate to the argument. Remove decorative
  imagery when requested rather than retaining it because an earlier version
  used it. Align supporting icons optically with the text or table they accompany;
  a warning icon usually precedes its label, and a link icon shares its baseline.
- Use consistent, light-gray references: “Title. Authors, Venue Year,” with the
  title italicized and one line per work when it fits. Keep authors and venue/year
  together. Check available width before shrinking text; use an approved short
  title when needed, with full metadata and locators in notes. Verify venues
  rather than silently labeling published work as a preprint.
- Default supporting citations to a shared footer baseline, stacking multiple
  works upward with consistent spacing. Page numbers should use the reference
  size and align with the content margin. Keep image credits beside their own
  images when association matters, compact enough not to displace the figure.
  Do not repeat a source on every slide in a clearly attributed sequence.
- Do not add citation icons automatically to every source credit. Follow the
  deck's approved convention; plain gray text is preferable for compact image
  credits. If used, keep icons modest and baseline aligned. Do not add citation
  icons to Paper or Code navigation links. Keep footer URLs visually secondary.

### Visual iteration and delivery

- Before modifying a slide or diagram, render its current version and inspect it.
  After each meaningful layout change, render the affected slide in isolation
  with the real theme and fonts and inspect it at its intended reading size.
  Successful compilation and old previews are not visual validation.
- Prefer independently previewable slides and shared definitions for related
  diagrams. Refresh the complete deck, notes, and handout before handing off a
  revision. Inspect affected handout pages as well as full-size slides; the user's
  primary review format must not lag behind the deck.
- Check padding, type hierarchy, baselines, title-to-figure gaps, column gutters,
  connector clearance, small figure labels, captions, and footer separation.
  Inspect neighboring builds together for unintended movement. Recheck the final
  render after the last spacing change.
- Record approved preferences, replacing superseded instructions instead of
  appending contradictory ones. Keep reusable rules here and exact wording,
  dimensions, paths, and one-off exceptions in the project-specific section.
  Occasionally ask for feedback on a concrete rendered alternative when a
  meaningful aesthetic choice remains; handle routine spacing fixes directly.
- When publication is requested, finish the visual review first, publish only the
  requested artifacts, and create requested montages/videos from that same final
  PDF. Check opening and closing frames. Keep unrelated repository changes out of
  the publication commit and report any output that remains from an older build.

---

# Presentation-specific: AdvGame

## Scope and sources

- Recreate all substantive content of the 31-slide legacy PDF/PPTX in `old/`,
  except material the user explicitly removes in later feedback.
  Keep those originals unchanged. Restore animation builds as separate frames.
- Open with the AdvGame title slide, then About me, the jailbreak examples, "How to defend against attacks?", the
  first overview, then Beam directly. Do not insert a separate
  "How to safety train a model" divider. The overview
  uses "This talk: AdvGame" and numbers three stages: Safety training of
  models, Learning the attacker, Learning the defender. Do not label it "Main focus". Beam is the background
  example under stage 1. Repeat the overview at each stage, highlighting the
  current one. Keep attack generation, judges, the attacker objective, and
  attacker online DPO together, then explain joint defense
  training and why the two objectives are not simple negatives. Results and
  extensions follow the defense method. Preserve original titles and wording
  within these blocks. Do not re-request approval for approved work. Leave
  uncommitted.
- Treat `old/` as the default authority for titles, body wording, capitalization,
  punctuation, emphasis, examples, and visual character. Format conversion,
  simpler styling, layout fixes, build splitting, and audience review do not
  authorize rewriting the author's voice. Preserve wording verbatim where
  possible, including informal titles and distinctive annotations.
- Split overlays by repeating the original title and distributing existing text
  before introducing new copy. Preserve original figures and semantic colors.
  Propose factual corrections separately with original/replacement wording and
  evidence; make the smallest necessary edit. Do not silently weaken or
  strengthen claims. Record approved edits, corrections, and additions distinctly.
- Compare every legacy slide for removed/rephrased content, not only topic or
  numerical parity. The restoration audit is `review/beam-first-proposal.txt`.
- Use the approved informative self-play titles, without the original `Part 1`
  prefix. The recurring numbered overview uses fixed positions and gray inactive stages.
- The user removed the entire attic and all following material. Do not restore
  generic SFT/RL, REINFORCE/PPO, PPO/GRPO, or response-based DPO refresher slides.
  Beam introduces the training ingredients in the main talk. Keep benign-compliance
  regressions alongside the main results and group the ablations together.
- For Beam, use harmful/harmless terminology in slides and spoken notes; do not
  introduce ISE or its control-layer codes. Keep full source names in the audit.
  Do not separate comparison models into Chinese/Western groups; highlight Beam.
- The speaker worked on main RL systems, focusing on the large reasoning run on
  10.5k GB300 GPUs, and leads OPD. Safety is not their primary current focus.
  Keep the run scale, OPD leadership, and safety-role context in speaker notes.
  The About me slide uses “Member of Technical Staff (RL and OPD)” on one line,
  spelling out the job title and abbreviating its focus. Set “(RL and OPD)” in
  the lighter gray detail color. Do not repeat the speaker's name beneath
  “About me”. Omit a captain label. Introduce Beam
  by saying the speaker was recently part of a team training a model with a
  large-scale safety-training effort. Do not imply that they led safety training.
  Beam is the speaker's current work at Reflection. AdvGame is earlier,
  exploratory research from their time at FAIR. Beam illustrates the standard
  approach and provides context for asking what lies beyond it; do not imply
  that Beam historically motivated the AdvGame research.
  First-version jailbreak data was a static collection of known and automated
  attacks; automated jailbreak generation did not run continuously during RL.
  This is user-supplied context. The talk targets the automated jailbreak subset,
  not the whole safety mixture or every example in the 7.6% jailbreak category.
- Explain the Beam judge inside the concrete Safety RL example, with its compact
  harmful/harmless pass/fail table. Keep context in the notes: conversation /
  previous turns, jailbreak / original seed intent, agentic task / unsafe action.
  Keep the Safety RL judge slide limited to the pass/fail table and a source-identified prompt excerpt. Keep training rewards distinct from
  evaluation, retaining Clarification and Incoherent in the evaluation notes.
  Do not add a judge to the Pareto plot. Scope its claim to observed models.
  Introduce Beam with the model summary, benchmark results, “Beam is safe”, then
  “More safety details in the report”, before the training recipe. The report
  slide uses the same linked report cutout peeking from the bottom and
  “About 40 pages on safety training and evaluations.” Keep the scope table above
  it, with aligned columns, bold row labels, gray detail, and a light background. Training is only one part of the report;
  omit the redundant Training list row. Use no periods on the scope fragments.
  Name biological weapons, chemical weapons, loss of control, cyber offense,
  conversational/agentic behavior, over-refusal, prompt injection, child safety,
  independent evaluations, and human/automated red-teaming.
- Retain About me, the model summary, and the recipe from the Beam presentation’s
  opening. Put About me immediately after the title slide. The user subsequently
  removed report contents and architecture; do not restore them. The full benchmark
  overview was explicitly restored in the latest visual pass.
  Omit token efficiency. After the Safety RL examples, use the transition
  “This talk: how do we go beyond static datasets and tasks?”, with the paper
  title, venue, and author portraits grouped beneath it, immediately before
  the Learning the attacker overview.
  Copy the source content and figures, adapting typography and spacing to this
  deck; do not import the unnumbered Reflection cover or another roadmap.
- Use the recipe diagram copied from
  `../2026-beam-presentation/figures/model-provenance.tex` in
  `figures/beam-lineage.tex`. Preserve Pretrained, Midtrained, Agentic SFT/RL,
  Alignment SFT/RL, MOPD SFT, and final Beam, including weight ancestry versus
  teacher supervision. Remove bold emphasis from its labels at the user’s request.
  Do not substitute a simplified two-branch diagram.
  Keep the clean recipe first, followed by two identical-geometry builds. On the
  first, show the six agentic domains in a blue rounded box below the diagram.
  Replace it on the next build with the eight alignment domains in a purple
  box in exactly the same position and dimensions. Mention Safety verbally;
  do not add a separate highlight build.
  Use the domain inventory from the Beam presentation's rl-domains.tex, verified
  against the report. Do not restore the separate safety-training arrow callout.
  Notes retain shared SFT data, general tool-use RL under alignment, and safety
  data mixed into Alignment SFT/RL and MOPD stages rather than a final phase.
- Introduce Safety SFT with its generation/filtering/training diagram, without
  a worked prompt/reasoning/response example on that introductory slide, then three
  fixed-layout pie/example slides: harmful direct requests, harmful jailbreaks,
  and harmless requests. Introduce Safety RL with the policy/environment loop
  and judge explanation, then four matching pie/example slides: single-turn,
  multi-turn, agentic, and jailbreak last. Show the chart from the start of each
  sequence; bold one legend entry at a time beside its example. Do not postpone
  the pie until after the examples or retain separate duplicate example slides.
- Keep source pie proportions, full colors, and geometry fixed across the category
  builds. Do not dim or outline slices; only bold the current legend entry.
  Keep a consistent modest gap after each example rather than reserving a large
  empty area for the longest prompt. Show the jailbreak example without a focus
  annotation. Do not repeat it with a “this talk” heading or add a pie arrow.
  Label constructed prompts as “Example,” with exact provenance in notes. Do not
  cite WildJailbreak on these examples. The harmless Linux prompt may use
  jailbreak-style framing without making the underlying request harmful.
- For SFT, emphasize iterative failure collection, generating safe responses,
  filtering and rewriting reasoning traces, and removing the supplied policy for
  training. Retain the Deliberative Alignment citation on the introductory SFT
  slide, distinguishing its general method from Beam's rewriting step.
- Explain in speaker notes why both stages need safety data: SFT does not guarantee
  every sampled response follows policy; RL trains on sampled behavior. Neither is a universal
  guarantee. Explain the static jailbreak dataset and the talk's automated subset
  on the jailbreak example build. Keep the Beam sources in notes.
- Omit the detailed "Safety behavior shifts during RL and distillation" slide,
  which the user explicitly removed. Give the frontier plot its own page, with
  labels close to their data points and short leaders. Preserve all data values.
- Keep the AdvPrompter developmental note light: learned input-adaptive attacks,
  a static dataset for defense fine-tuning, then joint attacker/defender training
  in AdvGame. The user explicitly declined full AdvPrompter notation and plots.
  When discussing static attack datasets for defender training, recall the Beam
  safety RL recipe. Distinguish AdvPrompter's SFT defense experiment from using
  a static pool of attacks as RL tasks.
  Do not imply that Beam used AdvPrompter. Distinguish target-response likelihood
  as an attack objective from judge-based evaluation. PAIR already used judge
  feedback in 2023, so do not claim judges began with AdvGame or that all earlier
  attacks optimized target strings. Keep the target-string/judge comparison
  qualitative and brief, before the cat-and-mouse motivation.
- Immediately before AdvPrompter, show the user-supplied ICML 2025 tutorial
  timeline with its bitmap title cropped out and the native frame title
  "Language model attack landscape, pre-2026", then repeat it with a native circle around
  AdvPrompter. Keep the source bitmap bytes unchanged.
  Credit Hamed Hassani, Amin Karbasi, and Alex Robey and link the tutorial.
  On the circled build, add a connected pop-out with the AdvPrompter title,
  all five coauthors' circular portraits, and their contribution marks.
  Use regular weight for every name; omit “Our paper”. Keep ICML 2025.
  Preserve the paper's stars on Anselm Paulus and Arman Zharmagambetov and
  daggers on Brandon Amos and Yuandong Tian. Use native photograph masks.
  Explain in speech that automated red-teaming for even one prompt was already
  challenging. AdvPrompter learned seed-conditioned attack generation against
  a fixed target before the joint training in AdvGame. Keep the historical
  claim scoped to an early input-conditioned attack generator, not the first
  learned red-teaming method. Keep the comparison figure light and qualitative.
- Explain AdvPrompter with two simple diagrams. First: multiple initial prompts → a
  shared AdvPrompter LLM, with the supplied attacker image → matching jailbreaks. Briefly
  name amortized optimization and cite Brandon Amos's tutorial. In speech,
  explain that optimizing even one jailbreak was costly, and learning a mapping
  shares computation across prompts. Second: learned attacker → static dataset
  of attacks and safe responses → defender safety fine-tuning. Preserve the
  distinction between its SFT defense experiment and static attack tasks in RL.
  Keep the block borders moderately thick, with neutral data boxes and restrained
  red/green role accents and pale fills. Match the supplied attacker image’s
  background to its block. Do not restore the dense target-likelihood feedback-loop diagram.
- Introduce attacker learning through preferences over the outcomes of two
  attacks before showing online DPO. Keep those slides adjacent, use a title
  that identifies the attacker. Omit the separate general attacker RL objective.
  Draw independent calls to the same defender, with matching rounded orthogonal
  branches and merges. Keep the fixed-model qualification in notes. Use the same
  visual grammar to introduce the defender’s response preferences immediately
  before its DPO loss. Use strict $\succ$
  consistently for illustrative preferences. The full method later explains the preferred-defender-response
  comparison and faithfulness gate; do not lose those qualifications.
- Start Learning the defender with one bridge showing Wong–Kolter's convex bounds and
  randomized smoothing side by side, then explain why a precisely defined
  perturbation set is harder for language: changes depend on meaning and context.
  Continue with AdvPrompter's static defense dataset, then the cat-and-mouse
  problem. Omit the separate Wong and smoothing detail slides. The user removed the Goodfellow/panda example
  entirely. Do not restore it, the red-block builds, or the sweater/cloak photo.
  Credit the smoothing image to Hassani, Karbasi, and Robey's ICML 2025 tutorial
  (PDF page 348), while crediting Cohen, Rosenfeld, and Kolter for the result.
  Put the two paper citations directly beneath their respective images on this
  bridge. Keep each paper title on one line using a concise title where needed,
  with authors and venue beneath. Put a smaller tutorial image credit centered above the smoothing image.
  Enlarge the images and keep the title/author spacing in each reference compact. Do not imply that all certification for restricted language settings is impossible.
- Keep the hope of subsuming earlier attacks in future work, not the method
  introduction. Human-defined collections and strategies may broaden coverage;
  distinguish that aspiration and optional extension from the evaluated recipe.
- Add AdvPrompter as a concrete example on the cat-and-mouse slide. Its defense
  experiment uses a static dataset; the general "Iterate" step is not a claim
  of joint online training in AdvPrompter. Write the zero-sum assumption as
  R_def = -R_att. Title that discussion "Can the defender negate the attacker's
  reward?" to make the actor explicit. Present attacker online DPO first, then say the defender uses
  the corresponding construction on response pairs. Keep paired example
  headings balanced and the full Linux-process question on one line.
- Primary paper: the ICML 2026 version of Safety Alignment of LMs via
  Non-cooperative Games, https://proceedings.mlr.press/v306/paulus26b.html.
  The sibling `../2025.advgame` is an older source checkout; do not silently
  prefer it over the published version. Use it for original vector figure assets.
- Beam evidence: read-only `../2026-beam-tr/chapters/safety.tex` and its figures.
  Explain SFT, mixed-task safety RL, and MOPD. The user removed the proposed
  AdvGame extension for Beam entirely; do not reintroduce it in future work,
  conclusions, or speaker notes.
- The user removed the Glimmer discussion and the standalone agent-risk
  slide. The user subsequently removed the OpenClaw image from Future work
  too. Keep the three text topics: broader attack coverage, prompt injection
  on agents, and other modalities, now combined with limitations on one slide. Do not imply a
  demonstrated application to Beam or Glimmer.
- Source corrections and all old-to-new mappings live in `review/parity.json`.
  Keep results, qualifications, and numerical relationships intact.

## Authoring and build

- One assembly: `advgame-presentation.tex` holds the shared preamble and ordered
  inputs. Each `slides/<stable-label>.tex` holds one `\talkslide` and adjacent
  `\speak` notes. Keep diagrams in reusable `figures/` files. Both views compile
  from the same assembly; do not duplicate slide content in a preview source.
- Use `styles/beamerthemebasic.sty`: white background, dark text, restrained blue,
  no Reflection green bars or branding. Keep a simple frame number footer.
  Use the supplied Keynote screenshots as visual inspiration: Source Sans Pro
  semibold charcoal headings, regular body text, bold lead-ins, and open spacing.
  Use the same charcoal (#404040) as the default text color throughout, including
  body text, math, and diagrams. Preserve semantic accents and gray references.
  The user rejected Black-weight headings. Use neutral lighter gray for secondary
  text, clearly distinct from the main text, rather than dark blue-gray.
  Source Sans Pro is a visual match, not a verified identification of the
  original Keynote font. Preserve all author names and circular portraits, and
  show `bamos.github.io/presentations` as a left-aligned, light-gray monospaced link
  with a baseline-aligned globe at the bottom of the opening and closing slides.
  Omit the website link from About me. On both bookends, put ICML 2026 in plain
  18-point charcoal text to the right of the title, separated by a modest vertical
  divider. Do not use a badge or a second venue caption beneath the title.
  Tighten the gap between portraits and names. Bold Brandon Amos only on
  the opening slide; keep his AdvPrompter and closing credits regular.
  Hide the frame number on About me, the title slide, all three overview builds,
  and the closing recap. Other page numbers align with the right
  content margin, not the physical page edge.
  The user favors a text overview with main ideas beneath three numbered
  headings. Use dark text for the current stage and gray for the others, without
  a colored bar. Beneath each heading, list the approved recap topics:
  “SFT, RL, and judges (e.g., as in Beam)”, with the parenthetical in lighter gray;
  “AdvPrompter, learned attacks, judge feedback”;
  “Joint training, separate rewards, robustness and utility”.
  Append “(online DPO)” to both learning headings on the same line, in regular
  weight and lighter gray. Do not repeat it in the recap details.
  Keep each description on one line. Headings and recap details use the same modest body size, with
  bold weight distinguishing headings. Align the details with the
  heading after its number, not with the number itself.
  In the first overview’s speaker notes, explain that Beam is the background
  example because the speaker is familiar with its pieces and they are fairly standard.
- Remove the manual-versus-automatic landscape comparison. The tutorial timeline
  builds instead use “Language model attack landscape, pre-2026”; preserve the circle
  around AdvPrompter on the second build.
- Omit a redundant source footer when a news screenshot already visibly identifies
  its source. Keep attribution in the notes.
- Go directly from the method to Experimental setup. The user removed the
  standalone Experimental Results divider, including its white replacement.
  The deck ends at the closing recap. Do not include an attic or other supplementary section.
- Prefer spaced prose statements to unordered bullet markers. Keep numbering
  when it expresses an actual sequence or the three-stage overview.
- The introductory Helpful/Harmless goal slides were removed. Do not restore
  their conversation layouts merely because the source files still exist.
- The author portraits use the shared native circular mask in
  `styles/author-portraits.tex`, without editing the underlying photographs.
  Preserve the paper's contribution stars on Anselm Paulus and Arman
  Zharmagambetov on the AdvGame title slide. Use the shared compact contribution
  mark command for stars and daggers, with no double-raised text asterisks.
  Keep the contribution footer omitted.
  Keep conference information on the title slide without Paper/Code links.
  The closing slide repeats the three-stage recap with all stages active.
  It has no paper screenshot or page number. Keep the closing presentations link
  left aligned, modest, and gray, with its globe icon.
  Use the shared bookend layout for the paper title, venue divider, portraits,
  and names. Lower the opening title/venue/author group slightly to balance its
  empty outline area without moving the footer. On the closing slide, left-align
  the outline with descriptions beneath their headings. Bracket the outline
  with matching light horizontal rules at the content margins, leaving space
  between the lower rule and the URL. Keep the paper title rather than “Thank you”.
- Declare reference metadata once in `styles/references.tex`. Use
  `\paperref{key}` or `\paperrefs{key1,key2}` for title, author, venue/year
  source lines. Omit displayed “arXiv” and generic “Technical report” venue
  labels; retain their years, links, and full metadata in notes. Use the short
  “Deliberative Alignment” title to keep its source on one line.
  Use “Title. Authors, Venue Year”, with an italicized title and the shared
  9-point light-gray `\referencefont` (body text is 11 point). Do not use em
  dashes between fields. Each work gets its own line or compact paragraph,
  stacked upward from the shared footer baseline. Never run consecutive
  works together or strand a year on its own line. Keep each book icon attached to its title, trim
  its transparent padding, align it vertically with the text, and use a compact gap.
  `\slideref{...}` and `\bookref{...}` remain the shared lower-level formatters.
  `\paperref`, `\paperrefs`, and `\bottompaperrefs` collect sources for the
  shared footer. Use `\inlinepaperref` only for an intentional inline credit,
  such as the image-linked references on the certification bridge.
  Keep explanatory parentheticals in lighter gray. Avoid duplicated formatting
  and oversized book emoji.
  Do not repeatedly cite AdvGame on slides explaining this talk's own method,
  implementation, or results. Keep its source locators in notes and cite
  other work where relevant.
- Combine the original Zou jailbreak and the supplied social-post example on
  one slide, citing Zou et al. (2023), Greedy Coordinate Gradient (GCG). Preserve
  the eyes emoji. The latest request is one additional slide for the full Claude
  screenshot, without a multi-slide buildup. Use the same visible title and
  GCG citation as the preceding example; do not add Appendix B to the slide.
  Keep the spoken treatment brief. Do not stack replacement text.
- Show the approved defense-stack "this talk" callout on a second physical frame,
  after the unannotated figure. Keep every other element fixed between the frames.
  This does not authorize restoring the removed pie-chart focus build.
  On the defense-stack builds, use the reference line alone for the baseline
  defenses paper; omit the paper screenshot and its "e.g." label.
- Use separate physical frames for builds. Do not stack replacement text or rely
  on PDF animation. Each frame gets a unique label and corresponding notes entry.
- Keep tables, equations, and explanatory diagrams editable. Original images and
  paper plots retain their intended display proportions, checking the PowerPoint
  crop and shape when an extracted image looks distorted. Split dense content
  before shrinking it.
- Disable automatic hyphenation on slides. Check title wraps, table headers,
  diagram arrow clearance, source lines, and body text at presentation size.
  Keep phrases together in long titles; avoid a lone final word. Adjust the
  line break without rewriting the title or shrinking its font.
- `make` builds slides, speaker notes, and the four-up, vector-preserving
  handout, refreshing all ignored root PDFs. `make handout` refreshes just
  the deck and handout.
  `make check` checks PDF bounds, frame/notes parity, and the build manifest.
  `make previews` renders all slides and notes into ignored `previews/`.
  `make preview SLIDE=<stable-label>` builds only the selected slide with the
  actual theme, producing PDF and PNG in `build/slide-previews/`. Multiple labels
  can be passed as a quoted space-separated list. Use this for every diagram
  iteration, then run the full build before delivery to refresh the handout.
  `scripts/slide_source.py` resolves slide inputs for the manifest checks.
- Use the local `.venv` (pymupdf and pillow) for asset extraction and validation.
  `latexmk` builds sequentially into `build/`. No workload lock is required.
- Keep sources in root, `slides/`, `styles/`, `scripts/`, `figures/`, `assets/`, and `review/`.
  Generated PDFs, renderings, and downloaded research stay local and ignored.
- Inspect all final slides and notes after the last change. Successful compilation
  alone does not establish readable layout or content parity.

## Content and audience review

- Audience assumption: ML researchers familiar with basic RL, new to AdvGame.
  Timing is provisional because this request did not specify a talk duration.
- Distinguish joint online training from literally simultaneous GPU updates.
  Separate parameter sharing from whether a game is zero-sum.
- Keep the faithfulness gate, compliance/deflection swap, and optimistic attacker
  comparison against each prompt's preferred defender response explicit.
- Pairwise judges can still fail. Judge-format ablations hold DPO fixed; comparing
  DPO against GRPO changes more than the judge. Do not claim universal superiority.
- Preserve the Qwen and Llama utility/compliance regressions. Distinguish fixed
  adversarial prompts from adaptive attacks and a ten-sample attack from one shot.
- State the paper's idealized tabular equilibrium argument separately from neural
  training convergence and certified robustness, neither of which is established.
- Distinguish the paper formulation from the released code. Its Qwen and Llama DPO
  configurations set `use_ema_model_as_ref_model: true`, substituting EMA log
  probabilities in the loss as well as using EMA for sampling. Do not claim the
  released DPO recipe has fixed loss references. The code uses 0.95 old + 0.05 new
  weights; Eq. (10) uses the opposite coefficient convention. Parameter EMA is
  not exact Nash-MD. Record related judge-conditioning and rubric differences in
  the source audit, without assuming released configs prove which run made a table.
- Use the compact score-gap form on both DPO slides. Show the loss above the plot
  and the score definition below it. The loss is the expectation of minus log
  sigmoid of preferred score minus rejected score; the score is beta times the
  log probability relative to the relevant reference policy.
  The score is not a pointwise judge reward. Preserve conditioning variables,
  the reference-policy role, and the same preferred/rejected notation. Keep setup and notation definitions in speaker notes; the slide shows
  the loss, plot, and score definition only. Omit the redundant
  “A relative log-probability score” caption.
- Use two consecutive “Putting it all together” slides: the original separate
  attacker/defender overview first, then the detailed joint rollout and losses.
  Place both after defender DPO. On the detailed slide, connect both within-attack response
  pairs to the compact defender DPO loss and the attack comparison to the matching
  attacker DPO loss beneath the horizontal diagram. Keep the faithfulness filter
  before defender rollouts and the comparison against each attack’s preferred
  defender response. Omit the visible EMA footnote; retain implementation context
  in notes. Do not restore the duplicate update build or the deleted attic.
- Preserve “A different paradigm: adversarial games”. Retain its supplied
  attacker/defender illustration, enlarged and centered with rounded corners,
  and keep only the top line on the slide. Move the three adaptation, shifting-attack-surface, and equilibrium points into notes.
- Explain a mechanism with a concrete example before dense equations. Use brief
  citations on slides and complete source locators in adjacent notes/comments.
- Review the final sequence as a new audience member. Check motivation, terminology,
  pacing, evidence, and transitions. Record suggestions separately from the slides.

## Latest presentation refinements

- Put AdvPrompter safety fine-tuning in Learning the defender, directly before
  The cat-and-mouse game problem. Show the two training phases on the static
  dataset graphic, then add the repeat loop on the next slide. Do not imply
  AdvPrompter itself performed joint online training. Omit “Current Practice.”
- Delete the redundant From AdvPrompter to AdvGame slide. Contextualize
  Self-RedTeam as prior online attacker–defender co-training before explaining
  the differences. The full paper title is Chasing Moving Targets with Online
  Self-Play Reinforcement Learning for Safer Language Models. Its game-outcome
  rewards are zero-sum; distinguish those from role-specific reward shaping.
  A new comparison table is only proposed, not approved for addition.
- Give self-play slides informative titles: “Self-RedTeam: same model, symmetric objective”
  and “Can one model learn to attack and defend?”
- Label comparison modules “Pairwise judge.” Omit obvious “illustrative
  preference” labels from diagrams; retain the qualification in speaker notes.
- Show both judges' preference comparisons consistently. In the joint rollout
  diagram, the defender outputs a preferred/rejected response pair for each
  attack; label the outgoing preferred response used to compare attacks.
  Do not show only a winner for one judge and a comparison for the other.
  Keep the whole diagram horizontal: two attacks per seed, two responses per
  attack. Use plain “Attack” labels, explaining the faithfulness gate separately.
  Curved incoming branches meet at a centered junction, then one horizontal
  arrow enters the judge. Do not draw a dot at the join. Keep the same geometry
  across all build frames.
- Align response labels in a column, indent the response text, and use quiet
  horizontal rules to group the comparison example. Keep parenthetical details gray,
  but substantive claims and explanations charcoal.
- Keep image captions ragged-right with natural spacing. Separate source
  credits from the substantive takeaway; do not allow long captions to push
  into body text. Align paired image headings and reserve equal padding.
- Visually inspect every new or revised slide after rendering. Check space
  between the title, subtitle, image, and body, not just clipping and bounds.
- The user primarily reviews the four-up handout. Refresh it on every normal
  build and inspect the affected handout pages, including paired figure captions
  and source credits. Do not deliver a fresh deck with a stale handout.

## Annotated-handout refinements (2026-11-17)

- The annotated handout is a review source, not a generated output to overwrite.
  Record every mark and action in `review/annotated-handout-2026-11-17.json`.
- Preserve the latest overview headings and details; the reviewed handout predates
  the approved move of gray “(online DPO)” onto each learning heading.
- Use a vertical focus leader on the defense-stack slide, matching the diagram's
  charcoal arrows. Use blue for the AdvPrompter timeline circle, leader, and pop-out.
- Keep Beam's parameter count and campaign figures at the same size and weight,
  below the frame-title size. Use the same body size for their descriptions.
  Show the total and active parameter counts in one line, without a repeated
  shorthand heading. Enclose the three campaign statistics in a rounded charcoal
  box with a moderately thick border. Inset “RL” into the upper border with white
  clearance around the label; do not repeat “for RL” in the GPU caption.
- Avoid repeated Beam report footers throughout its section. The linked report
  cutouts introduce and close the source. Retain detailed sources in notes and
  distinct external references such as Deliberative Alignment on the slide.
- Use “Defining the jailbreak objective” for the target-string/judge comparison.
  Add a short target-string example and gray method examples. Separate the two
  columns with a quiet rule. The judge-based examples are “(e.g., Self-RedTeam,
  AdvGame)”; omit the extra sentence about training both players. Preserve the
  distinction between attack objectives and judge-based evaluation.
- Use “Challenges with pointwise judges” and “Comparing responses with a pairwise
  judge” for the reward examples. Keep the two numbered challenges prominent,
  quoted response text compact, and the prompt question italicized. Do not
  restore “Challenge: How to score compliance/deflection?” or the old
  “Pointwise rewards” label. Keep the safety-rubric caveat in notes.
- Use “Learning the attacker: online DPO” and the matching defender title.
  Remove the obvious sentence saying online DPO learns from these pairs.
  Each role has one DPO slide with its score definition and compact score-gap loss
  together, separated by a softly outlined plot panel. Show one schematic score profile over output candidates, with the
  preferred and rejected outputs as individual points and vertical arrows. Label
  the vertical axis “Score”, matching the reference-relative log-probability
  definition. Annotate the policies and loss terms with short labels and thin
  gray leaders. The curve is not a density, and candidate ordering is arbitrary.
  Explain this in notes; do not show separate winner/loser distributions.
- On Self-RedTeam, show only the user-supplied attacker/defender/verifier image
  with its citation at the top beneath the title. Omit the harmful/benign split
  and extra explanatory text. Keep the shared-parameter and reward-shaping
  qualifications in notes. Omit repeated AdvPrompter footer references
  on the static-dataset and cat-and-mouse slides.
- Place model examples directly beside the corresponding attacker, defender,
  and judge descriptions. Use a ruled 2-by-2 reward matrix for the criterion swap.
- Remove the standalone faithfulness slide and the extra faithfulness-filter
  line on the defender preference slide. Keep the filter in the joint rollout
  diagram. Retain all
  short-circuit cases and the optimistic attacker comparison in speaker notes.
- Combine limitations and future work, retaining the lack of a robustness
  certificate, coverage limitations, asymmetry, and all three future directions.
  Use four full-width rows with consistent indented descriptions and light
  separators; do not put the final two topics side by side.

## Latest visual pass (2026-11-17)

- About me explicitly names Reflection AI beneath the job title. Vertically center
  the two-line text group with its logo.
- Use the user-supplied Google DeepMind and Intel Labs logos on About me
  (`assets/beam-intro/google-deepmind.png` and `intel-labs.png`). Preserve their
  proportions and balance their visual size with the enlarged Adobe Research mark.
- Include the full 22-benchmark overview copied from the Beam presentation, with
  all eight models and original values. Both decks use pale green through
  Reflection green (#1E3207), with row maxima at the darkest end. Put B or T
  directly beside every model-size value; do not leave the unit only at the left.
- Safety SFT uses the pie/example sequence described above, with no standalone
  WildJailbreak example or citation. Keep constructed-example provenance in notes.
- Draw Safety RL as the standard policy/environment action-and-observation loop,
  with the safety judge mapping a behavior label to reward for the update. Do not
  imply a learned world model. Omit the introductory SFT-versus-RL sentences and
  the “Alongside other tasks” callouts. Keep the mixed-data reminder and the
  distinction between SFT and RL in notes.
- Use “AdvPrompter: predicting adversarial prompts” on one line. Show multiple
  initial prompts and jailbreaks connected through one shared AdvPrompter LLM.
  Above it, use “Before: jailbreaking one prompt at a time” and “AdvPrompter:
  amortize the jailbreak across prompts”. A small definition box says “Amortized
  optimization: predicting the solution to optimization problems”. Remove
  “adversarial suffix” from the output boxes; use “Jailbreak” with matching indices.
- “Defining the jailbreak objective” uses “GCG and AdvPrompter” and no citation
  footer. Full references stay in notes. Put the observed verbosity reward hack in charcoal under the pointwise
  scoring example, without a standalone slide. The speaker observed high
  scores for verbose phrases, and the attacker learned to exploit them.
  Keep “But pairwise judges can still be exploited” in the notes.
- Preference diagrams flow vertically through two independent branches. Put the
  input on a short central stem joining a horizontal branch, with vertical arrows
  into both boxes and gently rounded corners. Avoid pointed splits and broad
  shallow curves immediately beneath the input label. Put the
  judged preference inside the pairwise-judge box; no extra output block or arrow.
  Use $x_s$ for the seed prompt, $x_1,x_2$ for attacks, and $y_1,y_2$ for sampled
  responses. Ordered candidates become $x_w,x_l$ or $y_w,y_l$ in the DPO loss.
  Carry the seed notation into the joint rollout and attacker conditioning.
  Preserve source figures verbatim and explain their original $s$ notation in notes.
- Define DPO notation directly in notes: rho_phi is the attacker, rho_ref the
  reference, x_s the seed, and c the class. Mirror this for the defender.
  Avoid “Let ... be”.
- Omit the visible EMA-rollout footnote. Retain source and implementation detail
  in speaker notes.

- Before the language-model attack landscape, introduce “What is an attack?” with an
  initial-prompt / attacker / modified-prompt diagram and the earlier GCG example.
  Explain intent preservation, possible initial refusal, and successful harmful
  compliance. Explain suffixes and semantically equivalent rewrites in speech, without the redundant visible sentence.
- Use matching 1.4pt Accent-blue strokes for the AdvPrompter timeline circle,
  connector, and pop-out border. Keep portrait borders governed by their own style.
- Use straight branches from the attack prompt to the two defender calls and
  from the seed to the two attacks in the joint rollout. Other established
  curved merges remain unchanged.
- On the certification comparison, omit book icons from the paired inline
  references. The smoothing image credit is gray “Image from Hassani et al., 2025”;
  the full tutorial citation and image locator remain in speaker notes.

## Latest layout refinements (2026-11-18)

- Keep equation annotation leaders clear of subscripts and brackets. Anchor their
  starts below the equation bounding box with a small visible gap, and mirror
  the spacing on attacker and defender DPO slides.
- The entire attic was removed, including its divider, full utility table,
  original algorithm, general RL objectives, EMA details, theory, and refreshers.
  End slides, notes, and handout at the closing recap.

## Publishing pass refinements (2026-11-18)

- Match the Agentic and Alignment data cards' heading and row gaps; preserve
  enough top padding above both headings
- Safety RL uses muted blue policy/update blocks, a warm neutral environment,
  and a sage safety judge, with unchanged charcoal arrows
- Keep both adaptive-attack model families on one table slide. Remove captions
  that merely narrate visible results; retain protocol and caveats in notes
- Use quiet blue callouts sparingly for substantive result qualifications or
  experimental distinctions, not for every table
- The later text-reduction pass removes the DPO setup sentence and its
  winner/loser annotations; retain the plot labels and equation annotations
- Slide numbers use the same shared font size as reference footers, with their
  established gray color and inset position
- Omit the duplicate “Jailbreak (this talk)” build. The unannotated jailbreak
  example leads directly into the beyond-static-datasets transition question


## Text-reduction pass (2026-11-19)

- Remove the Helpful/Harmless goal slides, TechBuzz article, and separate safety
  highlight build. Keep the actual jailbreak examples and alignment-data card
- Reintroduce the AdvGame paper title, author portraits, and ICML 2026 below the
  question on the beyond-static transition. Group the paper, venue, and all
  seven authors in a lightly shaded, rounded box with a modest blue border.
  Keep the paper title smaller than the question, in regular weight with only
  “AdvGame” emphasized. Align each row of author names to shared baselines and
  keep the venue-to-portrait gap modest. Do not repeat navigation links
- Prefer figures, tables, and concrete observations to narration that can be
  spoken. Do not replace removed prose with a new slogan or summary sentence
- The Safety RL judge slide shows the Beam training-rule table and an explicitly
  labeled excerpt from the released AdvGame judge prompt. Never attribute that
  code prompt to Beam. Reuse the table in the judge-based objective comparison
- Title the certification bridge “Why are defenses hard for language models?”
  Put the user's semantic attack-space explanation on two normal-body-size lines
  above a light horizontal divider, with “(among many others)” in gray. Keep the convex
  bounds image fully within the left column and leave a clear gap before the
  smoothing image. Keep detailed threat-set qualifications in speech
- On the adversarial-games slide, use only “Train both agents concurrently”
  above the large illustration
- Preserve the shared opening/closing layout specified under Authoring and build:
  a left-aligned 18-point title with only “AdvGame” emphasized, an 18-point venue
  across a vertical divider, all seven portraits, and the light-gray footer link.
  The closing recap adds the outline between matching horizontal rules.
- Use matching rounded orthogonal branches and merges in the attacker/defender
  preference diagrams. No broad shallow curves or join dots
- Self-RedTeam / Chasing Moving Targets is ICML 2026 (PMLR 306), not just the
  2025 preprint. Verify other venue changes before proposing them
- The Attacker in the Mirror is accepted at NeurIPS 2026; retain that venue
  in its displayed citation. GCG, Baseline Defenses, and Deliberative Alignment
  keep their preprint years until a venue is verified

- On the Beam recipe builds, keep the diagram slightly higher and horizontally
  centered at the same fixed position; center both data cards beneath it
- The safety-judge example omits the generic prompt opening. Show selected
  criteria for engaging with the query, constructive redirection, and deflection versus refusal in a
  teletype font, with the user-supplied transparent gavel centered beside the table.
  Omit the prompt instruction about response length
- The pointwise-judge challenge title starts with a small warning emoji aligned
  to the title text. Use two numbered challenges: absolute scores and reward hacks,
  with the observed verbosity example beneath the second. The next slide shows
  the pairwise comparison with an explicit informative title
- Keep the pointwise response table compact and inset so it supports the two
  challenges without dominating the slide. Use the same smaller response type on
  the following pairwise slide, a pale highlight for the preferred response, and
  two aligned comparisons beneath it. Preserve the example wording and keep
  the reward-hack observation in charcoal rather than red
