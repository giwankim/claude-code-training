---
theme: seriph
background: https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

addons:
  - slidev-component-progress
  - slidev-addon-asciinema
  - slidev-addon-qrcode
  - slidev-addon-bluesky

class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Claude Code Training
  
  By Kenneth Kousen
  
  Learn more at [KouseniT](https://kousenit.com)
drawings:
  persist: false
transition: slide-left
title: "Claude Code Training"
mdc: true
slidev:
  slide-number: true
  controls: true
  progress: true
css: unocss
---

<style>
.slidev-page-num {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  position: fixed !important;
  bottom: 1rem !important;
  right: 1rem !important;
  z-index: 100 !important;
  color: #666 !important;
  font-size: 0.875rem !important;
}
</style>

# Claude Code Training

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---

# Contact Info

Ken Kousen  
Kousen IT, Inc.

- ken.kousen@kousenit.com
- http://www.kousenit.com
- http://kousenit.org (blog)
- Social Media:
  - [@kenkousen](https://twitter.com/kenkousen) (twitter)
  - [@kenkousen@foojay.social](https://foojay.social/@kenkousen) (mastodon)
  - [@kousenit.com](https://bsky.app/profile/kousenit.com) (bluesky)
- *Tales from the jar side* (free newsletter)
  - https://kenkousen.substack.com
  - https://youtube.com/@talesfromthejarside

---

# Course Overview

<v-clicks>

- **Duration**: 5-hours
- **Topics Covered**:
  - Installation and CLI basics
  - Code exploration and understanding
  - Testing and quality assurance
  - Git operations and version control
  - Advanced features (Plan Mode, MCP, SDKs)
- **Hands-on Labs**: Multiple exercises with real codebases
- **Prerequisites**: Command-line experience, development background

</v-clicks>

---

# Pricing Plans

<v-clicks>

- **Pro Plan** - $20/month
  - ~10-40 prompts per 5 hours
  - Sonnet 4 only
- **Max Plan 5x** - $100/month
  - ~50-200 prompts per 5 hours
  - Sonnet or Opus 4
- **Max Plan 20x** - $200/month
  - ~200-800 prompts per 5 hours
  - Sonnet or Opus 4
- **Note**: Opus 4 uses 5x more credits than Sonnet 4
- **Limits reset**: Every 5 hours

</v-clicks>

📖 **Full details**: [Using Claude Code with your Pro or Max plan](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)

---

# What is Claude Code?

<v-clicks>

- Command-line AI tool for development
- Context-aware codebase understanding
- Autonomous and collaborative modes
- Multi-language support
- Integrated git operations
- Test generation and documentation

</v-clicks>

---

# Installation

<v-clicks>

- Install via npm: `npm install -g @anthropic-ai/claude-code`
- Or download from GitHub releases
- Set API key: `export ANTHROPIC_API_KEY="your-key"`
- Verify: `claude --version`

</v-clicks>

---

# Basic Usage

<v-clicks>

- Start Claude Code: `claude`
- Natural language prompts
- File-specific requests
- Multi-step workflows

</v-clicks>

---

# Operation Modes

<v-clicks>

- **Command Mode** (default) - Interactive conversation
- **Auto-Accept Mode** (Shift+Tab) - Autonomous execution
- **Plan Mode** (Shift+Tab+Tab) - Review plans before execution

</v-clicks>

---
layout: image-right
image: https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
backgroundSize: cover
---

# Core Productivity Features

<div class="text-center mt-20">
  <h2 class="text-4xl font-bold text-white bg-black bg-opacity-60 px-6 py-3 rounded-lg">
    Get Productive Immediately
  </h2>
  <p class="text-xl text-white bg-black bg-opacity-60 px-4 py-2 rounded mt-4">
    Essential features for daily development work
  </p>
</div>

---

# Code Exploration

<v-clicks>

- Find files, functions, patterns
- Understand system architecture
- Trace dependencies
- Identify frameworks
- Reference specific files with `@path/to/file.java`

</v-clicks>

```bash
"Analyze the UserService class"
"Explain @src/main/java/com/example/UserController.java"
"How does @pom.xml configure Spring Boot?"
```

---

# Test Generation

<v-clicks>

- Unit test creation
- Edge case identification
- Integration tests
- Mock object setup

</v-clicks>

```bash
"Create unit tests for the UserService"
"Add tests for error scenarios"
```

---

# Refactoring Capabilities

<v-clicks>

- Multi-file operations
- Smart refactoring
- Pattern replacement
- Modern syntax adoption

</v-clicks>

---
layout: image-right
image: https://images.unsplash.com/photo-1556075798-4825dfaaf498?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80
---

# Git Integration

<v-clicks>

- Commit message generation
- Branch management
- Merge conflict resolution
- Pull request creation

</v-clicks>

```bash
"Commit these changes with an appropriate message"
"Create a pull request for this feature"
```

---

# Multi-Tool Workflows

<v-clicks>

- **Batch operations**: Call multiple tools in single response
- **Parallel execution**: Run git status + diff + log simultaneously
- **Performance optimization**: Reduces round-trips
- **Complex workflows**: Chain dependent operations

</v-clicks>

```bash
# Parallel git operations
"Show me git status, recent commits, and current diff"

# Multi-file analysis
"Check all test files and their coverage simultaneously"
```

💡 **Pro tip**: Request "in parallel" for faster execution

---

# Documentation Generation

<v-clicks>

- Inline comments
- `README.md` files
- API documentation
- Architecture docs
- `CLAUDE.md` project configuration (covered later)

</v-clicks>

---

# Debugging Workflows

<v-clicks>

- Error message analysis
- Stack trace navigation
- Configuration debugging
- Integration debugging

</v-clicks>

---
layout: image-left
image: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
backgroundSize: cover
---

# Essential Workflow Tools

<div class="text-center mt-20">
  <h2 class="text-4xl font-bold text-white bg-black bg-opacity-60 px-6 py-3 rounded-lg">
    Customize Your Experience
  </h2>
  <p class="text-xl text-white bg-black bg-opacity-60 px-4 py-2 rounded mt-4">
    Session management and personalization
  </p>
</div>

---

# CLAUDE.md Files

<v-clicks>

- **Project memory**: `./CLAUDE.md` (shared with team)
- **User memory**: `~/.claude/CLAUDE.md` (personal preferences)
- Auto-discovered up directory tree
- **Quick add**: Start input with `#` to add memory
- **Commands**: `/memory` to edit, `/init` to bootstrap
- **Import files**: Use `@path/to/import` syntax

</v-clicks>

---

# Custom Statusline

<v-clicks>

- **Configure context display**: `~/.claude/settings.json` or `/statusline`
- Shows git branch, status, working directory, custom info
- Keeps important context visible without asking
- Reduces repetitive status checks

</v-clicks>

```json
{
  "statusline": {
    "items": [
      {"type": "git_branch"},
      {"type": "git_status"},
      {"type": "cwd"},
      {"type": "custom", "command": "node -v"}
    ]
  }
}
```

Perfect for teams wanting standardized context visibility

---

# Custom Slash Commands

<v-clicks>

- **Project scope**: `.claude/commands/` (shared with team)
- **User scope**: `~/.claude/commands/` (personal, use `/user:command`)
- **Filename becomes command name** (e.g., `service.md` → `/service`)
- Quick shortcuts for common workflows

</v-clicks>

---

# Creating Slash Commands

<v-clicks>

- **Project commands** are shared with the entire team
- **User commands** are personal and require `/user:` prefix
- **Use `$ARGUMENTS`** for dynamic content in commands

</v-clicks>

```bash
# Project commands (shared with team)
mkdir -p .claude/commands
echo "Create service for $ARGUMENTS entity" > .claude/commands/service.md

# User commands (personal)
mkdir -p ~/.claude/commands  
echo "Fix issue #$ARGUMENTS" > ~/.claude/commands/fix.md

# Usage: /service User  or  /user:fix 123
```

Real-world example - a powerful, personal documentation command:
```markdown
# ~/.claude/commands/docs.md
Update both the README.md and CLAUDE.md files as appropriate.
If either file does not exist, please create it. Generate the
CLAUDE.md file as though the user invoked the init task.
```

---

# Hooks & Automation

<v-clicks>

- **Configure shell commands** that execute on tool calls
- **user-prompt-submit-hook**: Pre-process prompts before execution
- **Security controls**: Validate and filter operations
- **Workflow automation**: Chain commands for complex tasks
- **Location**: Configure in settings or project-specific hooks

</v-clicks>

```bash
# Example: Auto-format before edits
echo 'prettier --write $1' > .claude/hooks/pre-edit.sh

# Example: Validate commits
echo 'npm test && npm run lint' > .claude/hooks/pre-commit.sh
```

Treat hook feedback as user input - adjust if blocked

---

# Resuming Conversations

<v-clicks>

- **`--continue`**: Automatically resume most recent conversation
- **`--resume`**: Interactive picker showing conversation history with timestamps and message counts
- **Full history restored**: Complete message context maintained (even hundreds of messages)
- **Original settings preserved**: Model and configuration retained
- **Stored locally**: Complete conversation database maintained on your machine

</v-clicks>

```bash
# Continue most recent conversation
claude --continue

# Show conversation picker with details
claude --resume

# Continue with new prompt
claude --continue --print "Continue with my task"
```

---
layout: image-right
image: https://images.unsplash.com/photo-1586953208448-b95a79798f07?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80
---

# Working with Images

<v-clicks>

- **Drag and drop** images into Claude Code window
- **Copy/paste** with `Ctrl+V` (not `Cmd+V` even on a Mac!)
- **Provide file path**: "Analyze this image: `/path/to/screenshot.png`"
- Analyze UI designs, error screenshots, diagrams
- Generate code from visual mockups
- Debug visual issues and layouts

</v-clicks>

```bash
# Common image workflows
"Analyze this error screenshot and suggest fixes"
"Generate HTML/CSS for this UI mockup"
"Explain what this diagram shows"
"Convert this whiteboard sketch to code"
```

---

# Jupyter & Data Science Support

<v-clicks>

- **Read .ipynb files** with full cell outputs
- **Analyze notebooks**: Code, markdown, and visualizations
- **Edit notebook cells**: Use NotebookEdit tool
- **Data analysis workflows**: Process datasets and results
- **Visualization understanding**: Interpret charts and graphs

</v-clicks>

```bash
"Analyze this Jupyter notebook and explain the data pipeline"
"Add error handling to the data processing cells"
"Convert this notebook to a production Python script"
```

---
layout: image-right
image: https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
backgroundSize: cover
---

# Advanced Features

<div class="mt-20">
  <h2 class="text-4xl font-bold text-white bg-black bg-opacity-60 px-6 py-3 rounded-lg">
    Power User Capabilities
  </h2>
  <p class="text-xl text-white bg-black bg-opacity-60 px-4 py-2 rounded mt-4">
    Complex features for sophisticated workflows
  </p>
</div>

---
layout: image-right
image: https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80
---

# Extended Thinking

<v-clicks>

- Trigger deeper analysis with "think" in your prompts
- Use **"think more"**, **"think harder"**, **"ultrathink"** for deeper reasoning
- Shows thinking process as *italic gray text*
- Perfect for complex architectural decisions
- **Verification pattern**: "Before you finish, verify your solution and fix any issues"
- **Note**: Thinking tokens count toward usage but provide higher quality results

</v-clicks>

```bash
# Examples of extended thinking prompts
"Think deeply about the best approach for implementing OAuth2 in our API. 
Before you finish, verify your solution and fix any issues."

"Think harder about potential security vulnerabilities in this code"
"Think more about the tradeoffs between these two design patterns"
```

---

# Plan Mode

<v-clicks>

- Press `Shift+Tab+Tab` to activate
- Claude presents implementation plan
- Review strategy before execution
- Approve or modify approach
- Perfect for complex changes

</v-clicks>

---

# Model Context Protocol (MCP)

<v-clicks>

- Standard protocol for AI-to-system connections
- Tool integration (APIs, databases, services)
- Context enhancement for better AI responses
- Security controls and permissions

</v-clicks>

---

# MCP Configuration

<v-clicks>

### Import from Claude Desktop
```bash
claude mcp add-from-claude-desktop
```
Automatically imports MCP servers from Claude Desktop config

### Manual Configuration
```bash
# Project-scoped (default)
claude mcp add <server-name>

# User-scoped (available across all projects)
# Remote HTTP transport
claude mcp add --transport http context7 https://mcp.context7.com/mcp
# Local execution
claude mcp add context7 -- npx -y @upstash/context7-mcp

# Management commands
claude mcp list
claude mcp remove <server-name>
```

### Config Locations
- **Claude Desktop**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Claude Code (project)**: `.mcp.json` in project root

</v-clicks>

---

# MCP Server Examples

<v-clicks>

- **GitHub MCP** - Repository operations, issues, PRs
- **Context7** - Downloads latest API docs and examples for modern code
- **Docker MCP Toolkit** - Container management and operations
- **Playwright MCP** - UI test generation and browser automation
- **Heroku MCP** - Deployment and app management

</v-clicks>

---

# Setting Up MCP Servers

<v-clicks>

- Interactive setup: `claude mcp`
- Local servers: Full configuration control
- Remote servers: OAuth authentication, zero maintenance
- Docker MCP Toolkit: `docker mcp gateway run`

</v-clicks>

```bash
# List existing MCP servers
claude mcp list

# Add local server
claude mcp add my-server -e API_KEY=123 -- /path/to/server

# Add remote server (HTTP)
claude mcp add --transport http remote-server https://example.com/mcp

# Add Docker MCP toolkit
claude mcp add docker-mcp docker mcp gateway run
```

---

# Claude Code SDKs

<v-clicks>

- **Available SDKs**: TypeScript, Python, Command Line
- **Build AI-powered coding assistants** into your workflows
- **Multi-turn conversations** and session management
- **Custom system prompts** and flexible I/O formats
- **MCP integration** for extended capabilities

</v-clicks>

```bash
# Command line usage
claude -p "Write a function to calculate Fibonacci numbers"
claude -p "Generate a hello world function" --output-format json
```

```typescript
// TypeScript SDK
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Write a haiku about foo.py",
  options: { maxTurns: 3 }
})) {
  // Process messages
}
```

---

# SDK Real-World Examples

<v-clicks>

### Python Integration
```python
from claude_code import query
async for msg in query("Refactor this module",
                       context_files=["app.py"],
                       max_turns=3):
    print(msg.content)
```

### CI/CD Pipeline
```yaml
# GitHub Actions example
- name: AI Code Review
  run: |
    claude -p "Review PR changes" --output-format json > review.json
```

### Git Hooks
```bash
#!/bin/bash
# .git/hooks/pre-commit
claude -p "Check for security issues" --allowed-tools read,grep
```

</v-clicks>

---
layout: image-left
image: https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
backgroundSize: cover
---

# Management & Control

<div class="mt-20">
  <h2 class="text-4xl font-bold text-white bg-black bg-opacity-70 px-6 py-3 rounded-lg">
    Monitor and Control
  </h2>
  <p class="text-xl text-white bg-black bg-opacity-70 px-4 py-2 rounded mt-4">
    Cost, context, and permission management
  </p>
</div>

---

# Cost Monitoring

<v-clicks>

- Use `/cost` command to check usage
- Shows current usage and limits
- Pro Plan: Displays prompt count vs limit
- Max Plans: Shows monthly usage summary
- Limits reset every 5 hours
- Plan ahead for intensive work sessions

</v-clicks>

```bash
# Check your current usage
/cost

# Example output (Pro Plan):
# 📊 Cost information:
#    - Input tokens: 1,245
#    - Output tokens: 3,782
#    - Total cost: $0.076

# Example output (Max Plan):
# With your Claude Max subscription, no need to monitor cost
# — your subscription includes Claude Code usage
```

---

# Context Management

<v-clicks>

- Use `/compact` command to compress conversation history
- Claude Code automatically compacts when context limit approaches
- Warning message appears before auto-compaction
- Preserves essential information while reducing token usage
- Manual compaction gives you control over timing

</v-clicks>

```bash
# Manually compact the conversation
/compact

# Warning message example:
# ⚠️ Context limit approaching. Auto-compacting in next response
# to preserve conversation history and continue working.
```

---

# Smart Context Management

<v-clicks>

- **Auto-compaction**: Automatic when approaching limits
- **Warning messages**: Advance notice before compaction
- **Preservation strategy**: Keeps essential information
- **Manual control**: Use `/compact` proactively
- **Long conversations**: Maintains context over hundreds of messages

</v-clicks>

```bash
# Warning you'll see:
⚠️ Context limit approaching. Auto-compacting in next response
to preserve conversation history and continue working.

# Proactive management:
/compact  # Compress conversation manually
```

---

# Configuring Permissions

<v-clicks>

- **Fine-grained control** over Claude Code's capabilities
- **Use `/permissions` UI** to manage tool permissions
- **Allow/Deny rules** for specific tools and actions
- **Enterprise policies** for organization-wide control
- **Permission precedence**: Enterprise → CLI → Project → User

</v-clicks>

```bash
# Example permission rules
Bash(npm run test:*)     # Allow npm test commands
Edit(docs/**)           # Allow editing docs directory
Read(src/*)             # Allow reading source files

# Access permissions UI
/permissions
```

---

# Permission Patterns

<v-clicks>

### Common Permission Profiles
- **Development Mode**: Full access for active coding
- **Review Mode**: Read-only for code reviews
- **Safe Mode**: Limited tools for sensitive operations
- **CI/CD Mode**: Specific tools for automation

</v-clicks>

```bash
# Quick permission profiles via aliases
alias claude-dev='claude --allowed-tools all'
alias claude-review='claude --allowed-tools read,grep'
alias claude-safe='claude --disabled-tools bash,webfetch'
alias claude-ci='claude --allowed-tools bash,git,test'
```

---
layout: image-left
image: https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
backgroundSize: cover
---

# Team & Best Practices

<div class="text-center mt-20">
  <h2 class="text-4xl font-bold text-white bg-black bg-opacity-60 px-6 py-3 rounded-lg">
    Collaborate Effectively
  </h2>
  <p class="text-xl text-white bg-black bg-opacity-60 px-4 py-2 rounded mt-4">
    Team workflows and professional practices
  </p>
</div>

---

# Git Worktrees for Parallel Sessions

<v-clicks>

- Check out multiple branches into separate directories
- Run Claude Code sessions independently on each branch
- Share git history while isolating working files
- Perfect for multi-feature development

</v-clicks>

```bash
# Create worktrees for parallel work
git worktree add ../project-feature-a -b feature-a
git worktree add ../project-bugfix bugfix-123

# Run Claude Code in each directory
cd ../project-feature-a && claude
cd ../project-bugfix && claude

# Manage worktrees
git worktree list
git worktree remove ../project-feature-a
```

---

# Effective Prompting & Best Practices

<div class="grid grid-cols-2 gap-8">
<div>

### Effective Prompting
<v-clicks>

- **Be specific** about what you want to achieve
- **Provide context** about your goals and constraints
- **Use iterative refinement** for complex tasks
- **Include examples** when possible to show desired patterns

</v-clicks>

</div>
<div>

### Best Practices
<v-clicks>

- **Create a git branch first** for any significant changes
- **Commit checkpoints regularly** during development
- **Review all AI-generated code** before accepting
- **Test generated code** thoroughly

</v-clicks>

</div>
</div>

---

# Troubleshooting & Configuration

<v-clicks>

### System Health Check
```bash
claude /doctor  # Diagnose installation issues
```

### Global Configuration
```bash
claude config set -g model claude-sonnet-4
claude config set -g verbose true
claude config set -g max_conversation_turns 10
```

### Check Current Settings
```bash
claude config list  # View all settings
echo $ANTHROPIC_API_KEY  # Verify API key
```

</v-clicks>

---

# Security & Permissions

<v-clicks>

### Security-Focused Aliases
```bash
# Safe mode - limited tools
alias claude-safe='claude --allowed-tools read,write,edit'

# Review mode - read-only
alias claude-review='claude --allowed-tools read,grep'

# Development mode - all tools
alias claude-dev='claude --allowed-tools all'
```

### Tool Restrictions
```bash
# Disable specific tools
claude --disabled-tools bash,webfetch

# Allow only specific tools
claude --allowed-tools read,write,edit,task
```

</v-clicks>

---

# Common Issues & Solutions

<v-clicks>

### Installation Problems
- **Command not found** → Check PATH: `npm list -g @anthropic/claude-code`
- **Permission denied** → Use correct npm prefix or sudo
- **Windows users** → WSL is required (Claude Code doesn't run natively on Windows)

### Runtime Issues
- **API key not found** → Set `ANTHROPIC_API_KEY` environment variable
- **Rate limits** → Use `/cost` to monitor usage
- **Context too large** → Use `/compact` to reduce conversation size

### Quick Fixes
```bash
# Reinstall globally
npm uninstall -g @anthropic/claude-code
npm install -g @anthropic/claude-code

# Alternative: Direct binary
curl -fsSL https://storage.googleapis.com/anthropic-releases/claude-cli/install.sh | bash
```

</v-clicks>

---

# Development Process

<v-clicks>

- Start with clean git state
- Generate tests if none exist
- Commit checkpoints regularly
- Use Claude for git workflows (commits, issues, merges)
- Use git worktrees for parallel sessions on different branches
- Review changes before accepting
- Test generated code thoroughly

</v-clicks>

---

# Team Collaboration

<v-clicks>

- Share `CLAUDE.md` configurations
- Document successful patterns
- Review AI-generated code together
- Establish team conventions

</v-clicks>

---

# Quick Access

<div class="grid grid-cols-2 gap-8 mt-8 place-items-center">
  <div class="flex flex-col items-center">
    <h3>Claude Code Docs</h3>
    <QRCode
      :width="200"
      :height="200"
      type="svg"
      data="https://docs.anthropic.com/en/docs/claude-code/overview"
      :margin="5"
      :dotsOptions="{ type: 'rounded', color: '#3b82f6' }"
    />
    <p class="text-sm mt-2">docs.anthropic.com/claude-code</p>
  </div>
  <div class="flex flex-col items-center">
    <h3>Course Repository</h3>
    <QRCode
      :width="200"
      :height="200"
      type="svg"
      data="https://github.com/kousen/claude-code-training"
      :margin="5"
      :dotsOptions="{ type: 'rounded', color: '#10b981' }"
    />
    <p class="text-sm mt-2">github.com/kousen/claude-code-training</p>
  </div>
</div>

---

# Important Links

<div class="mt-8 space-y-6 text-xl">

<v-clicks>

### 📚 Claude Code Documentation
`https://docs.anthropic.com/en/docs/claude-code`

### 🐙 Official GitHub Repository  
`https://github.com/anthropics/claude-code`

### 💻 Course Source Code & Exercises
`https://github.com/kousen/claude-code-training`

### 🆘 Support & Issues
`https://github.com/anthropics/claude-code/issues`

</v-clicks>

</div>

---

# Community & Social

<div class="flex flex-col items-center mt-4">
  <div class="max-w-md mx-auto scale-90">
    <Bluesky id="at://did:plc:dfl6zqxuwaytxeyankzivs76/app.bsky.feed.post/3lsmcosqat22d" />
  </div>
  
  <p class="text-center mt-2 text-gray-500 text-sm">
    Follow the Claude Code community for updates and tips
  </p>
</div>

---

# Thank You!

<div class="text-center">

## Questions?

<div class="pt-12">
  <span class="text-6xl"><carbon:logo-github /></span>
</div>

**Kenneth Kousen**  
*Author, Speaker, Java & AI Expert*

[kousenit.com](https://kousenit.com) | [@kenkousen](https://twitter.com/kenkousen)

</div>