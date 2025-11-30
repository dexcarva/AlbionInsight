# Project Roadmap

**[Leia em Português](Roadmap.pt-BR.md)**

This roadmap outlines the planned features and improvements for Albion Insight. The timeline is approximate and may change based on community contributions and priorities.

## Current Version: 0.1.0 (Initial Release)

### Implemented Features
- ✅ Cross-platform support (Linux, Windows, macOS)
- ✅ Real-time network packet capture
- ✅ Basic Photon Protocol decoding
- ✅ Damage meter structure and UI
- ✅ Session management (start, stop, reset, save)
- ✅ Money and fame tracking
- ✅ Basic combat event tracking

## Version 0.2.0 (Q1 2026) - Enhanced Combat Tracking

### Goals
- Complete implementation of core combat events
- Improved damage meter accuracy
- Enhanced UI for combat statistics

### Planned Features
- [ ] Full implementation of `CastHit` event
- [ ] Full implementation of `Attack` event
- [ ] Healing tracking improvements
- [ ] Buff and debuff tracking
- [ ] Ability cooldown tracking
- [ ] Combat log viewer
- [ ] Real-time DPS graph
- [ ] Configurable damage meter columns

### Technical Improvements
- [ ] Unit tests for event handlers
- [ ] Performance optimization for packet processing
- [ ] Memory usage optimization
- [ ] Error handling improvements

## Version 0.3.0 (Q2 2026) - Data Persistence and Analysis

### Goals
- Add persistent storage for session history
- Provide historical data analysis tools
- Export functionality enhancements

### Planned Features
- [ ] SQLite database for session storage
- [ ] Session history browser
- [ ] Statistical analysis of past sessions
- [ ] Comparison between sessions
- [ ] Export to CSV format
- [ ] Export to JSON format
- [ ] Export to Excel format
- [ ] Automatic session backup

### Technical Improvements
- [ ] Database schema design
- [ ] Migration system for database updates
- [ ] Data visualization library integration
- [ ] Caching layer for performance

## Version 0.4.0 (Q3 2026) - Advanced Features

### Goals
- Implement advanced tracking features from the original tool
- Add dungeon-specific tracking
- Enhance player information display

### Planned Features
- [ ] Dungeon tracker
- [ ] Dungeon entry timer
- [ ] Map history tracking
- [ ] Player information panel
- [ ] Guild activity tracking
- [ ] Loot logger
- [ ] Rare item notifications
- [ ] Fame per hour calculator

### Technical Improvements
- [ ] Event caching system
- [ ] Improved state management
- [ ] Plugin architecture foundation
- [ ] API documentation

## Version 0.5.0 (Q4 2026) - Crafting and Economy

### Goals
- Add crafting calculator
- Implement auction house data tracking
- Provide economic analysis tools

### Planned Features
- [ ] Crafting calculator
- [ ] Material cost analysis
- [ ] Profit margin calculator
- [ ] Auction house price tracking
- [ ] Market trend analysis
- [ ] Item price history
- [ ] Trade tracking
- [ ] Economic dashboard

### Technical Improvements
- [ ] External API integration
- [ ] Data synchronization
- [ ] Background data updates
- [ ] Notification system

## Version 1.0.0 (2027) - Stable Release

### Goals
- Feature parity with original tool
- Stable, production-ready release
- Comprehensive documentation

### Planned Features
- [ ] All major features from AlbionOnline-StatisticsAnalysis
- [ ] Comprehensive event coverage
- [ ] Multi-language UI support
- [ ] Customizable themes
- [ ] Advanced configuration options
- [ ] Cloud sync (optional)
- [ ] Mobile companion app (optional)

### Technical Improvements
- [ ] Full test coverage
- [ ] Continuous integration/deployment
- [ ] Automated release process
- [ ] Performance benchmarking
- [ ] Security audit
- [ ] Code documentation
- [ ] API stability guarantees

## Long-Term Vision (Post 1.0)

### Community Features
- Plugin marketplace
- Community-contributed event handlers
- Shared session analysis
- Leaderboards (optional, privacy-respecting)

### Advanced Analytics
- Machine learning for play pattern analysis
- Predictive analytics for market trends
- Automated recommendations for improvement

### Integration
- Discord bot integration
- Web dashboard
- Streaming overlay support
- Third-party tool integration

## How to Contribute to the Roadmap

We welcome community input on the roadmap! Here's how you can contribute:

1. **Vote on Features**: Comment on existing feature requests in GitHub Issues
2. **Suggest Features**: Open a new issue with the "enhancement" label
3. **Implement Features**: Pick an item from the roadmap and submit a PR
4. **Provide Feedback**: Share your thoughts on prioritization

## Roadmap Principles

Our roadmap follows these principles:

1. **Community-Driven**: Features are prioritized based on community needs
2. **Stability First**: We won't sacrifice stability for new features
3. **Cross-Platform**: All features must work on all supported platforms
4. **Open Source**: All features remain free and open source
5. **Privacy-Respecting**: No data collection without explicit user consent

## Tracking Progress

You can track the progress of roadmap items through:
- [GitHub Milestones](https://github.com/dexcarva/AlbionInsight/milestones)
- [GitHub Projects](https://github.com/dexcarva/AlbionInsight/projects)
- [Changelog](../CHANGELOG.md)

---

*This roadmap is subject to change based on community feedback and contributions.*

*Last updated: November 30, 2025*
