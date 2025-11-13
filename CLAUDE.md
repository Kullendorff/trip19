Purpose & context
Johan (the owner) is developing an extensive Swedish-language Delta Green tabletop RPG campaign called "Trip 19/Svarta Madonnan" (Black Madonna) for his gaming group. This ambitious 8-12 session campaign combines historical research with supernatural horror, blending the real 1940 Pennsylvania Central Airlines Flight 19 crash (which killed Senator Ernest Lundeen) with an adapted KULT scenario set in Leningrad 1942. The campaign represents a sophisticated evolution from previous one-shot adventures ("The Mall Before Christmas," "Sea Glass") into a research-driven, slow-burn mystery that avoids typical "world-ending urgency" in favor of intellectual curiosity and gradual revelation.
The project centers on five main player characters forming a Delta Green "Outlaw" cell in the Washington DC area: Mac Riley (FBI agent on forced leave), Father Sullivan (Navy Chaplain with crisis of faith), Kai "Sparky" Zhang (NSA analyst/former hacktivist), Sam "Trench" Novak (USAR specialist), and Hanna Engler "Scalpel" (medical examiner). Johan collaborates with players Jonas (Mac), Daniel (Hanna Engler), and Andreas (Sullivan), emphasizing authentic character development over dramatic convenience. The campaign's unique approach involves players conducting real Google research using genuine historical documents, with supernatural elements seamlessly filling documented gaps in the historical record.
Current state
Johan has completed comprehensive character development for multiple team members, creating detailed documentation systems covering stats/skills, backgrounds, relationships, professional capabilities, and psychological states. Recent work focused on balancing game mechanics (standardizing 74-75 stat points, 460 professional skill points), developing character websites with Swedish translations, and creating practical reference materials including biblical quotations for Sullivan and technical specifications for Sparky's hacking capabilities.
The campaign structure is well-established, connecting Nazi crystal technology from Trip 19 to supernatural events through the recurring antagonist Volkov. Johan has compiled extensive real archival sources (CAB reports, FBI files, university collections) that players can research, with fictional annotations creating authentic investigation experiences. Character trauma and psychological deterioration from previous operations drive individual stakes, particularly Mac's PTSD and obsession with Volkov, and Sullivan's shattered faith after witnessing supernatural transformations.
On the horizon
Johan is developing the campaign transition from domestic archival research to international investigation spanning Germany and Russia, requiring careful coordination of character motivations and operational logistics.
Future development includes completing the Black Madonna integration, establishing how players move from historical research to physical investigation sites, and creating handouts that blend genuine historical quotes with fictional supernatural elements. Johan also plans to expand beyond one-shots into longer campaign structures while maintaining the research-driven approach that distinguishes this project from typical Delta Green scenarios.
Key learnings & principles
Johan has established that authenticity trumps dramatic convenience in character development, consistently requesting realistic boundaries over Hollywood portrayals (particularly regarding hacking capabilities and federal law enforcement procedures). He emphasizes that players should develop characters themselves rather than receiving excessive narrative content, preferring fact-based presentations that allow organic character growth.
The campaign philosophy centers on blending factual research with supernatural horror, where players never know what's real versus fictional until they investigate. This approach requires careful balance between documented historical gaps and fictional elements, ensuring supernatural explanations feel like natural extensions of real mysteries rather than arbitrary additions.
Character trauma and psychological deterioration serve as primary narrative drivers, with sanity loss and breaking bonds central to long-term Delta Green experiences. Johan has learned that comprehensive character documentation (separate artifacts for different aspects) facilitates both web development and campaign management while maintaining consistency across multiple sessions.
Approach & patterns
Johan follows a systematic character development process: balancing game mechanics first, then developing narrative elements, establishing practical details, defining relationships, creating presentation materials, and producing supplementary player resources. He consistently requests separate artifacts for different character aspects to facilitate web development and file management.
Research integration involves identifying real historical sources players can access, then layering supernatural elements underneath authentic documentation. Johan emphasizes Swedish language consistency throughout materials while maintaining technical accuracy for specialized domains (military procedures, federal law enforcement, cybersecurity capabilities).
Character websites follow standardized structures with sidebar navigation, responsive design, and thematic color schemes appropriate to each character's background. Johan provides specific corrections on translations and cultural elements, ensuring materials serve Swedish gaming groups while depicting American settings accurately.
Tools & resources
Johan utilizes comprehensive Delta Green RPG source materials and maintains detailed project knowledge systems for character continuity. He references real historical archives including CAB investigation reports, university collections (Stanford, Iowa), National Archives, and FBI FOIA materials for authentic research experiences.
Technical development involves Claude Code for website creation, Midjourney for character image generation (using specific profile parameters), and systematic markdown documentation for character information management. Johan accesses genuine historical podcasts (Rachel Maddow's "Ultra"), government documents, and archival sources to ground fictional elements in documented reality.
The project incorporates real-world locations throughout the DC/Maryland/Virginia area, with Johan researching actual addresses and facilities to provide authentic operational contexts for character activities and campaign logistics.

Website structure
The Trip 19 project is organized as a multi-page website with a clear hierarchy:

**Root level (index.html):**
- Landing page featuring the "TRIP 19" campaign title with "Chesapeake Cell" designation
- Grid layout displaying all five main characters with portraits, names, callsigns, roles, and brief descriptions
- Card-based navigation linking to individual character pages
- Dark theme with orange accent colors (#ff6b35), Volkov background overlay
- Fully responsive design with mobile breakpoints
- Footer showing operation status, security clearance, and last updated date

**Character directories (Mac/, Sullivan/, Sparky/, Scalpel/, Trench/):**
Each character has a dedicated folder containing:
- **index.html** - Main character sheet with stats, skills, background, and timeline
- **Multiple specialized pages** covering different aspects:
  - Operational details (operativt.html)
  - Personal information (personligt.html)
  - Professional background (karriär.html, pastoral.html, tekniskt.html)
  - Reference materials (bibelcitat.html for Sullivan, technical_guide.html for Sparky)
  - Investigation boards (volkov_board.html for Mac)
- **Character images** in various contexts (portraits, tactical, operational)
- **Supporting documentation** (markdown files with detailed background, bonds, timeline)
- **Optional style.css** (Mac has external stylesheet, others use inline styles)

**Common design patterns across character pages:**
- **Sidebar navigation** (280px fixed width):
  - Character name and role in header
  - Page link container with bordered, hoverable navigation buttons
  - Active page highlighted with accent color background
  - Quick navigation section with anchor links to page sections
  - Footer with "TRIP 19 → CHESAPEAKE CELL" link back to main page
  - Sticky positioning for persistent navigation
- **Main content area:**
  - Hero section combining character introduction with large portrait image
  - Content sections with consistent styling (border, padding, dark background)
  - Tables for stats and detailed information
  - Stats grids displaying primary attributes (STR, CON, DEX, INT, POW, CHA)
  - Skills grids showing proficiency percentages
  - Timeline sections with visual markers
  - Responsive grid layouts adapting to screen size
- **Styling approach:**
  - CSS custom properties (variables) for theme colors unique to each character
  - Mac: Steel blue (#4A90A4) - investigation noir theme
  - Sullivan: Copper/bronze (#b87333) - pastoral/military theme
  - Sparky: Tech-focused color scheme
  - Dark backgrounds (#0D1117, #0A0F0F ranges) across all characters
  - Consistent spacing, typography, and component patterns
  - Lightbox functionality for enlarging images
  - Hover effects and smooth transitions
  - Mobile-first responsive breakpoints (768px, 480px)

**Technical implementation:**
- Pure HTML/CSS with minimal JavaScript (lightbox functionality, smooth scrolling)
- No external frameworks or dependencies
- Inline styles in <style> tags within HTML files (except Mac which uses external style.css)
- Swedish language throughout interface and content
- Accessible semantic HTML structure
- Print-friendly styling considerations